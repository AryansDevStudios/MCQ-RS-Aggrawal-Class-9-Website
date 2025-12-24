
import re
import json

def parse_mcq(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()


    # print(f"DEBUG: Content length: {len(content)}")
    blocks = re.split(r'(\*\*\d+\.\*\*)', content)
    # print(f"DEBUG: Blocks found: {len(blocks)}")
    
    questions = []
    
    # blocks[0] is header
    # blocks[1] is "**1.**"
    # blocks[2] is question content 1
    # blocks[3] is "**2.**"
    # ...
    
    current_q = None
    
    for i in range(1, len(blocks), 2):
        if i+1 >= len(blocks): break
        
        q_num_str = blocks[i].strip('*').strip('.') # "1"
        q_content_raw = blocks[i+1].strip()
        
        lines = q_content_raw.split('\n')
        
        question_text_lines = []
        options = []
        correct_answer_idx = -1
        correct_answer_char = ''
        
        # Parse lines
        # Looking for (a) ..., (b) ..., (c) ..., (d) ...
        # And "**Correct Answer:** (x)"
        
        opt_pattern = re.compile(r'^\(([a-d])\)\s+(.*)')
        ans_pattern = re.compile(r'\*\*Correct Answer:\*\*\s*\(([a-d])\)')
        
        # We need to handle multi-line questions and options
        # Strategy: 
        # 1. Extract Correct Answer from the end.
        # 2. Extract options (d), (c), (b), (a) in reverse order or standard order.
        
        # Find Correct Answer first
        lines_reversed = list(reversed(lines))
        ans_found = False
        remaining_lines = []
        
        for line in lines_reversed:
            line = line.strip()
            if not line: continue
            
            if not ans_found:
                m = ans_pattern.search(line)
                if m:
                    correct_answer_char = m.group(1)
                    ans_found = True
                    continue # Don't add this line to remaining
            
            remaining_lines.insert(0, line)
            
        # Now parse options from remaining_lines
        # We expect options to be at the bottom.
        
        parsed_options = {} # 'a': text, 'b': text...
        
        # We will scan from bottom up for options (d), (c), (b), (a)
        # However, for 76-79 and 80-81, options might be missing.
        
        # Standard flow
        current_opt_char = None
        current_opt_text = []
        
        # Check if it's an Assertion Reason type (76-79) or Match (80-81) by checking if we find (a) (b) (c) (d)
        has_options = False
        for line in remaining_lines:
            if re.match(r'^\([a-d]\)', line):
                has_options = True
                break
        
        if not has_options:
            question_text = "\n".join(remaining_lines)
            if "Assertion" in question_text:
                 # Standard Assertion Reason Options
                 options_list = [
                     "Both A and R are true and R is the correct explanation of A.",
                     "Both A and R are true but R is not the correct explanation of A.",
                     "A is true but R is false.",
                     "A is false but R is true."
                 ]
            elif "Match the following" in question_text:
                # We need to construct the correct answer string from the q_content or just use the correct ans char
                # Wait, for 80, Correct Answer is a generic map like `(a)-(r)...`.
                # But in `data.js` we need an array of options.
                # I'll create a single correct option and 3 distractors.
                # Actually, reading the text for 80: "**Correct Answer:** (a)-(r), (b)-(s), (c)-(q), (d)-(p)"
                # My regex above might have failed because the Value was complex?
                # Let's re-read the prompt text for 80:
                # "**Correct Answer:** (a)-(r), (b)-(s), (c)-(q), (d)-(p)"
                # My regex `\*\*Correct Answer:\*\*\s*\(([a-d])\)` expects single char.
                # So for 80, I will manual handle or improve regex.
                pass 
            
            # If we didn't extract options, we handle below
        
        # Let's try to extract options
        
        final_q_text_lines = []
        captured_options = {}
        
        # Loop lines to find options
        # We assume options start with (a), (b), (c), (d) at start of line
        
        parsing_options = False
        curr_opt = None
        
        for line in remaining_lines:
            m = opt_pattern.match(line)
            if m:
                # New option found
                parsing_options = True
                curr_opt = m.group(1)
                captured_options[curr_opt] = m.group(2)
            elif parsing_options:
                # Continuation of current option (if any) or text?
                # Usually options are single line. If not, append.
                if curr_opt:
                    captured_options[curr_opt] += " " + line
            else:
                # Question text
                final_q_text_lines.append(line)
                
        question = "\n".join(final_q_text_lines).strip()
        
        # Post-Processing for specific missing option cases
        option_array = []
        
        # Mapping for output
        map_char_to_idx = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        
        if correct_answer_char and correct_answer_char in map_char_to_idx:
            ans_idx = map_char_to_idx[correct_answer_char]
        else:
            # Maybe the correct answer line was complex (like Q80)
            # Find the complex correct answer line from the original block?
             ans_idx = 0 # Default/Fallback
             
        # Check if we have 4 options
        if len(captured_options) == 4:
            for c in ['a', 'b', 'c', 'd']:
                option_array.append(captured_options.get(c, ""))
        else:
            # Handle special cases (Assertion/Reason or Matching)
            if "Assertion (A)" in question:
                 option_array = [
                     "Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A)",
                     "Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A)",
                     "Assertion (A) is true but Reason (R) is false",
                     "Assertion (A) is false but Reason (R) is true"
                 ]
                 # Implicitly these map to a,b,c,d
            elif "Match the following" in question:
                # Read the full correct answer line again from raw block to extraction
                # For Q80: "**Correct Answer:** (a)-(r), (b)-(s), (c)-(q), (d)-(p)"
                # Just find the line starting with Correct Answer
                ca_line = ""
                for l in lines:
                    if "**Correct Answer:**" in l:
                        ca_line = l.replace("**Correct Answer:**", "").strip()
                        break
                
                # Use this as the correct option (index 0)
                # And create 3 fakes
                correct_opt_text = ca_line
                fake1 = correct_opt_text.replace("p", "x").replace("q", "y") # Lazy fake
                fake2 = "Different matching"
                fake3 = "None of these"
                
                # But wait, the user said "Correct Answer: (a)-(r)..."
                # This string IS the correct answer content. 
                # If I put it in option A, and set correct answer to 0 (A), that works.
                option_array = [correct_opt_text, "Incorrect Match 1", "Incorrect Match 2", "Incorrect Match 3"]
                ans_idx = 0
            else:
                 # Fallback
                 option_array = ["Option A", "Option B", "Option C", "Option D"]
        
        questions.append({
            "id": int(q_num_str),
            "question": question,
            "options": option_array,
            "answer": ans_idx
        })


    with open('d:/Mathematics Book MCQ/parsed_data.json', 'w', encoding='utf-8') as f_out:
        json.dump(questions, f_out, indent=2)


if __name__ == "__main__":
    parse_mcq('d:/Mathematics Book MCQ/temp_raw_data.txt')
