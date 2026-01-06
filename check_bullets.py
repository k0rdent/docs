#!/usr/bin/env python3
import os
import re
from pathlib import Path

def check_bullet_lists(file_path):
    """Check for missing blank lines before or after bulleted lists."""
    issues = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            return issues
        
        i = 0
        while i < len(lines):
            line = lines[i]
            # Check if line starts with a bullet point (with optional leading whitespace)
            if re.match(r'^\s*[-*+]\s', line):
                # Found start of a bullet list
                list_start = i
                
                # Check if there's a blank line before (unless it's the first line)
                if list_start > 0:
                    prev_line = lines[list_start - 1].rstrip('\n\r')
                    # If previous line is not blank and not a header, we might need a blank line
                    if prev_line.strip() and not prev_line.strip().startswith('#'):
                        issues.append(f'Line {list_start + 1}: Missing blank line before bullet list')
                
                # Find the end of the bullet list
                list_end = list_start
                # Look ahead to find where the list ends
                while list_end < len(lines) - 1:
                    next_line = lines[list_end + 1]
                    # If next line is also a bullet, continue
                    if re.match(r'^\s*[-*+]\s', next_line):
                        list_end += 1
                    # If next line is blank, the list might end here
                    elif not next_line.strip():
                        # Check if there's another bullet after the blank line (sub-list)
                        # For now, consider blank line as end of list
                        break
                    # If next line is indented (continuation of bullet item), continue
                    elif next_line.strip() and (next_line.startswith(' ') or next_line.startswith('\t')):
                        # Check if it's indented content (not a new bullet at different indent)
                        if not re.match(r'^\s{4,}[-*+]\s', next_line):  # Not a nested bullet
                            list_end += 1
                        else:
                            break
                    else:
                        # Next line is regular text, list ends here
                        break
                
                # Check if there's a blank line after the list
                if list_end < len(lines) - 1:
                    # Find next non-blank line
                    next_idx = list_end + 1
                    while next_idx < len(lines) and not lines[next_idx].strip():
                        next_idx += 1
                    
                    if next_idx < len(lines):
                        next_line = lines[next_idx]
                        # If next line is not a header and not blank, we need a blank line
                        if next_line.strip() and not next_line.strip().startswith('#'):
                            issues.append(f'Line {list_end + 1}: Missing blank line after bullet list')
                
                i = list_end + 1
            else:
                i += 1
                
        return issues
    except Exception as e:
        return [f'Error reading file: {e}']
    
    return issues

# Find all markdown files
md_files = []
for root, dirs, files in os.walk('.'):
    # Skip hidden directories
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for file in files:
        if file.endswith('.md'):
            md_files.append(os.path.join(root, file))

# Check each file
files_with_issues = []
for md_file in sorted(md_files):
    issues = check_bullet_lists(md_file)
    if issues:
        files_with_issues.append((md_file, issues))

# Print results
if files_with_issues:
    for file_path, issues in files_with_issues:
        print(f'{file_path}:')
        for issue in issues:
            print(f'  {issue}')
        print()
else:
    print('No issues found.')

