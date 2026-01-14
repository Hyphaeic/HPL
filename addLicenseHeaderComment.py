import os

# The license header to apply
HEADER = """/*
 * Copyright 2026 Hyphaeic SPC.
 *
 * Licensed under the Hyphaeic Public License, Version 1.0 (the
 * "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 *
 * https://github.com/hyphaeic/hpl
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

"""

# Unique string to check if license is already applied
CHECK_STRING = "Licensed under the Hyphaeic Public License"

# Extensions to target
TARGET_EXTENSIONS = [".rs"]

# Directories to skip (optional)
SKIP_DIRS = ["target", ".git"]

def apply_header_to_files(root_dir="."):
    count = 0
    skipped = 0

    print(f"Scanning directory: {os.path.abspath(root_dir)}...")

    for root, dirs, files in os.walk(root_dir):
        # Filter out directories we want to skip
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for filename in files:
            if any(filename.endswith(ext) for ext in TARGET_EXTENSIONS):
                filepath = os.path.join(root, filename)
                
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Check if the license is already there
                    if CHECK_STRING in content:
                        print(f"Skipping (already present): {filepath}")
                        skipped += 1
                        continue

                    # Write the header + original content
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(HEADER + content)
                    
                    print(f"Applied license to: {filepath}")
                    count += 1

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    print("-" * 30)
    print(f"Process complete.\nApplied: {count}\nSkipped: {skipped}")

if __name__ == "__main__":
    # You can change "." to specific folders like "./src" if you prefer
    apply_header_to_files(".")
