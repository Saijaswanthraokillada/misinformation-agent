import argparse
from PIL import Image
import pytesseract
from qdrant_utils import insert_claim, search_claim

def extract_text_from_image(image_path: str) -> str:
    """Extract text from an image using OCR."""
    img = Image.open(image_path)
    return pytesseract.image_to_string(img).strip()

def run_demo():
    print("=== Misinformation Detection Agent ===")
    print("Commands:")
    print("  insert <text>       → Add a claim")
    print("  search <text>       → Search by text")
    print("  search_img <path>   → Search by image")
    print("  exit                → Quit\n")

    while True:
        cmd = input(">> ").strip()
        if cmd.lower() == "exit":
            break
        elif cmd.startswith("insert "):
            text = cmd[len("insert "):]
            insert_claim(text)
        elif cmd.startswith("search "):
            text = cmd[len("search "):]
            search_claim(text)
        elif cmd.startswith("search_img "):
            path = cmd[len("search_img "):]
            extracted = extract_text_from_image(path)
            print(f"\n🧾 Extracted Text: {extracted}")
            search_claim(extracted)
        else:
            print("Unknown command. Use 'insert <text>', 'search <text>', or 'search_img <path>'.")

if __name__ == "__main__":
    run_demo()