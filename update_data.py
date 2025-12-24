
import json

def update_data():
    js_path = 'd:/Mathematics Book MCQ/src/data.js'
    json_path = 'd:/Mathematics Book MCQ/parsed_data.json'
    
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    with open(json_path, 'r', encoding='utf-8') as f:
        new_questions = json.load(f)
        
    # Find start of Chapter 1 questions
    # matches id: 1 ... title: "Number Systems" ... questions: [
    
    start_marker = 'questions: ['
    
    # We assume Chapter 1 is the first one, which is true in the file
    start_idx = js_content.find(start_marker)
    if start_idx == -1:
        print("Could not find questions array start")
        return

    # Find the closing bracket for this array.
    # We need to balance brackets starting from start_idx + len(start_marker)
    
    open_brackets = 0
    search_start = start_idx + len(start_marker)
    end_idx = -1
    
    # Since we are inside the array [ ... ], we start with count 1 (the one we just passed)
    # Actually, let's start scanning from search_start.
    # The 'questions: [' includes the opening bracket.
    
    open_brackets = 1
    
    for i in range(search_start, len(js_content)):
        char = js_content[i]
        if char == '[':
            open_brackets += 1
        elif char == ']':
            open_brackets -= 1
            if open_brackets == 0:
                end_idx = i
                break
                
    if end_idx == -1:
        print("Could not find matching closing bracket")
        return
        
    # Construct new content used for replacement
    # new_questions is a list of dicts. We need to format it as JS/JSON.
    # json.dumps produces valid JS object notation for this simple data (keys are strings, which is valid JS).
    # indent=4
    
    new_json_str = json.dumps(new_questions, indent=2)
    
    # Replace
    # We keep "questions: " part from the start marker effectively?
    # No, start_idx points to "q" of "questions".
    # We want to replace everything from `[` to `]` (inclusive).
    
    # range to replace: start_idx + len("questions: ") to end_idx + 1
    
    prefix = js_content[:start_idx + len("questions: ")]
    suffix = js_content[end_idx+1:]
    
    # The prefix ends with space after colon? "questions: [" 
    # Wait, start_marker was "questions: ["
    # So prefix should be js_content[:start_idx] + "questions: "
    
    # Resizing
    # text before 'questions: ['
    pre_text = js_content[:start_idx]
    
    # text 'questions: '
    # We want to replace [ ... ] with new [ ... ]
    
    new_content = pre_text + "questions: " + new_json_str + suffix
    
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Updated src/data.js successfully")

if __name__ == "__main__":
    update_data()
