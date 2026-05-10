import os

def save_iteration_snapshot(content: str, iteration: int, folder: str = "final_resumes"):
    """
    Saves the resume text to a specified folder with a versioned filename.
    """
    try:
        # Ensure the directory exists
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        file_name = f"resume_version_{iteration}.txt"
        file_path = os.path.join(folder, file_name)
        
        # Ensure content is a string
        if not isinstance(content, str):
            # If it's a Pydantic model, use model_dump to get a string
            if hasattr(content, "model_dump_json"):
                content = content.model_dump_json(indent=4)
            else:
                content = str(content)
                
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"--- Snapshot Saved: {file_path} ---")
        return file_path
    except Exception as e:
        print(f"Error saving file: {e}")
        return None
    
def safe_read_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return content if content else ""
    except FileNotFoundError:
        print(f"File not found: {path}")
        return ""
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return ""
