import json

def create_prompt_only_format(text):
    """Convert text to prompt-only format."""
    return {"prompt": [{"role": "user", "content": text}]}

def create_lm_format(text):
    """Convert text to language modeling format with both user and assistant messages."""
    return {
        "messages": [
            {"role": "user", "content": text},
            {"role": "assistant", "content": "Your GroundTruth Response."}  # Placeholder response
        ]
    }

# Specify the input and output file paths
input_path = "data/lean/Lean-Workbook/lean_workbook.json"
prompt_only_output = "data/lean/Lean-Workbook/lean_workbook_prompt_only.jsonl"
lm_output = "data/lean/Lean-Workbook/lean_workbook_lm.jsonl"

# Load the original JSON file
with open(input_path, "r", encoding="utf-8") as infile:
    data = json.load(infile)

# Write the prompt-only format to its file
with open(prompt_only_output, "w", encoding="utf-8") as outfile:
    for item in data:
        text = item.get("natural_language_statement", "")
        json.dump(create_prompt_only_format(text), outfile)
        outfile.write("\n")

# Write the language modeling format to its file
with open(lm_output, "w", encoding="utf-8") as outfile:
    for item in data:
        text = item.get("natural_language_statement", "")
        json.dump(create_lm_format(text), outfile)
        outfile.write("\n")

print(f"Prompt-only format saved to: {prompt_only_output}")
print(f"Language modeling format saved to: {lm_output}")