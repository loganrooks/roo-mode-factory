Okay, AI Coding Agent. Here is a detailed plan to implement the enhanced memory bank system with external formats, schema validation, and improved robustness. You will start with no prior context of this project besides the files you are explicitly asked to read.

**Phase 1: Initialization and Setup**

1.  **Goal:** Understand your tools and the existing memory bank scripts.
2.  **Action:** Read the following files to populate your context:
    *   `<read_file><path>.roo/.systemprompt</path></read_file>`
    *   `<read_file><path>.roo/rules-code/.clinerules-code</path></read_file>`
    *   `<read_file><path>.roo/scripts/update_memory_bank.py</path></read_file>`
    *   `<read_file><path>.roo/scripts/read_memory_bank.py</path></read_file>`
    *   `<read_file><path>.roo/scripts/version_control.py</path></read_file>`
    *   `<read_file><path>pyproject.toml</path></read_file>` (To check for dependencies later)

**Phase 2: Create Configuration Files**

1.  **Goal:** Create the external configuration files for formats and schemas.
2.  **Action:** Create the directory `.roo/config/` if it doesn't exist.
3.  **Action:** Create `memory_formats.yaml`.
    *   Use `write_to_file`. Ensure the path is correct.
    *   Content: (Provide the example YAML content from the previous plan, starting with `# filepath: /home/rookslog/zlibrary-mcp/.roo/config/memory_formats.yaml`)
        ````yaml
        # filepath: /home/rookslog/zlibrary-mcp/.roo/config/memory_formats.yaml
        # Defines formatting templates for memory bank entries

        # --- Core File Formats ---
        active_context:
          default: |
            ### [{timestamp}] - {title}
            - **Focus:** {focus}
            - **Actions:** {actions} # Script should handle if 'actions' is a list or string
            - **Status:** {status}
            ---

        global_context:
          Product Context: |
            #### [{timestamp}] - {title}
            - **Goal:** {goal}
            - **Initial State:** {initial_state}
            - **{phase_name} Focus:** {phase_focus}
            ---
          System Patterns: |
            #### [{timestamp}] - {title}
            ```mermaid
            {diagram}
            ```
            - **Description:** {description}
            ---
          Decision Log: |
            #### [{timestamp}] - Decision: {title}
            - **Context:** {context}
            - **Decision:** {decision}
            - **Justification:** {justification}
            - **Alternatives Considered:** {alternatives}
            ---
          Progress: |
            #### [{timestamp}] - {title}
            - **Status:** {status}
            - **Deliverables:** {deliverables}
            {notes_section} # Placeholder for optional notes section
            ---

        feedback:
          default: |
            ### [{timestamp}] - Source: {source}
            - **Issue/Feedback**: {issue}
            - **Analysis**: {analysis}
            - **Action Taken/Learnings**: {action}
            ---

        maintenance:
          Maintenance Log: | # Special table handling needed in script
            | {timestamp} | {action} | {description} |
          Known Issues: |
            - [{timestamp}] {issue_description} (Status: {status})
          Structure Changes: |
            - [{timestamp}] {change_description}
          Future Improvements: |
            - [{timestamp}] {improvement_idea}

        # --- Mode-Specific Formats ---
        sparc:
          Delegations Log: |
            ### [{timestamp}] Task: {task_name}
            - Assigned to: {mode_slug}
            - Description: {description}
            - Expected deliverable: {deliverable}
            - Status: {status}
            - Completion time: {completion_time}
            - Outcome: {outcome}
            - Link to Progress Entry: {progress_link}
          Workflow State: |
            ### Workflow State Update - [{timestamp}]
            - Current phase: {phase}
            - Phase start: {timestamp}
            - Current focus: {focus}
            - Next actions: {actions}
            - Last Updated: {timestamp}

        tdd:
          Test Plans: # Special handling for nested lists
            _header: | # Template for the overall plan entry header
              ### Test Plan: {title} - {timestamp}
            _unit_test_item: | # Template for each unit test item in the list
              - Test Case: {description} / Expected: {expected} / Status: {status}
            _integration_test_item: | # Template for each integration test item
              - Test Case: {description} / Expected: {expected} / Status: {status}
            _edge_case_item: | # Template for each edge case item
              - {description}: {test_approach}
          Test Coverage Summary: |
            ### Coverage Update: [{timestamp}]
            - **Overall**: Line: {line}% / Branch: {branch}% / Function: {function}%
            - **By Component**: `{components}`
            - **Areas Needing Attention**: {attention_areas}
          Test Fixtures: |
            ### Fixture: {fixture_name} - [{timestamp}]
            - **Purpose**: {purpose} / **Location**: `{location}` / **Usage**: {usage}
          TDD Cycles Log: |
            ### TDD Cycle: {feature_component} - [{timestamp}]
            - **Start**: {start_time} / **End**: {end_time}
            - **Red**: {red_description}
            - **Green**: {green_description}
            - **Refactor**: {refactor_description}
            - **Outcomes**: {outcomes}
          Test Execution Results: |
            ### Test Run: [{timestamp}]
            - **Trigger**: {trigger} / **Env**: {env} / **Suite**: {suite}
            - **Result**: {result} / **Summary**: {summary}
            - **Report Link**: {report_link} / **Failures**: {failures}

        code:
          Implementation Notes: |
            ### Implementation: {feature_component} - [{timestamp}]
            - **Approach**: {approach}
            - **Key Files Modified/Created**: {files}
            - **Notes**: {notes}
          Technical Debt Log: |
            ### Tech Debt: {issue_name_id} - [Status: {status}] - [{timestamp}]
            - **Identified**: {identified_time}
            - **Location**: `{location}`
            - **Description**: {description} / **Impact**: {impact} / **Priority**: {priority}
            - **Proposed solution**: {solution}
            - **Resolution Notes**: {resolution} / **Resolved Date**: {resolved_date}
          Dependencies Log: |
            ### Dependency: {dependency_name} - [{timestamp}]
            - **Version**: {version} / **Purpose**: {purpose} / **Used by**: {components} / **Config notes**: {config_notes}
          Code Patterns Log: |
            ### Code Pattern: {pattern_name} - [{timestamp}]
            - **Description**: {description} / **Example Usage**: {example_usage} / **Rationale**: {rationale}

        # --- Other Modes ---
        spec-pseudocode:
          Functional Requirements: |
            ### Feature: {feature_name} - [{timestamp}]
            - Description: {description}
            - Acceptance criteria: {acceptance_criteria} # List or string
            - Dependencies: {dependencies}
            - Status: {status}
          System Constraints: |
            ### Constraint: {constraint_name} - [{timestamp}]
            - Description: {description}
            - Impact: {impact}
            - Mitigation strategy: {mitigation_strategy}
          Edge Cases: |
            ### Edge Case: {feature_component} - [{timestamp}]
            - Scenario: {scenario}
            - Expected behavior: {expected_behavior}
            - Testing approach: {testing_approach}
          Pseudocode Library:
            _header: |
              ### Pseudocode: {component_feature} - {function_name} - [{timestamp}]
            _content: |
              ```pseudocode
              {pseudocode}
              ```
            _tdd_anchors_item: |
              - Test case: {description}

        architect:
          System Diagrams: |
            ### Diagram: {diagram_name} - [{timestamp}]
            - Description: {description}
            ```mermaid
            {diagram_code}
            ```
            **Notes:** {notes}
          Component Specifications: |
            ### Component Specification: {component_name} - [{timestamp}]
            - **Responsibility**: {responsibility}
            - **Dependencies**: {dependencies}
            - **Interfaces Exposed**: {interfaces_exposed}
            - **Internal Structure (Optional High-Level)**: {internal_structure}
          Interface Definitions: |
            ### Interface Definition: {interface_name} - [{timestamp}]
            - **Purpose**: {purpose}
            #### Method/Endpoint: {method_endpoint_name}
            - Input: {input} / Output: {output} / Behavior: {behavior} / Security: {security_notes}
          Data Models: |
            ### Data Model: {model_name} - [{timestamp}]
            - **Purpose**: {purpose}
            - **Structure**: {structure} # JSON or similar
            - **Relationships**: {relationships}

        # ... Add formats for debug, security-review, docs-writer, integration, monitor, devops, ask, memory-bank-doctor based on their .clinerules files ...
        # Example for security-review:
        security-review:
          Security Findings Log: |
            ### Finding: {finding_id} - {short_description} - [Status: {status}] - [{timestamp}]
            - **Severity**: {severity} / **Components**: {components} / **Description**: {description} / **OWASP**: {owasp} / **PoC**: {poc} / **Remediation**: {remediation} / **Resolved**: {resolved_time}
          Threat Models: |
            ### Threat Model: {component_feature} - [{timestamp}]
            - **Diagram**: {diagram_link_desc} / **Boundaries**: {boundaries} / **Actors**: {actors}
            - **Threats**: {threats_list} # List of threat objects/strings
          # ... etc ...

        # ... Add other modes similarly ...
        ````
4.  **Action:** Create `memory_schemas.yaml`.
    *   Use `write_to_file`. Ensure the path is correct.
    *   Content: (Provide the example YAML content from the previous plan, starting with `# filepath: /home/rookslog/zlibrary-mcp/.roo/config/memory_schemas.yaml`)
        ````yaml
        # filepath: /home/rookslog/zlibrary-mcp/.roo/config/memory_schemas.yaml
        # Defines JSON Schema validation rules for memory bank updates

        # --- Core File Schemas ---
        active_context:
          default:
            type: object
            properties:
              title: { type: string }
              focus: { type: string }
              actions: { type: [string, array], items: { type: string } } # Allow string or list of strings
              status: { type: string }
              timestamp: { type: string, format: date-time } # Added by script if missing
            required: [title, focus, status]

        global_context:
          Product Context:
            type: object
            properties:
              title: { type: string }
              goal: { type: string }
              initial_state: { type: string }
              phase_name: { type: string }
              phase_focus: { type: string }
              timestamp: { type: string, format: date-time }
            required: [title, goal]
          System Patterns:
            type: object
            properties:
              title: { type: string }
              diagram: { type: string } # Mermaid code
              description: { type: string }
              timestamp: { type: string, format: date-time }
            required: [title, diagram]
          Decision Log:
            type: object
            properties:
              title: { type: string }
              context: { type: string }
              decision: { type: string }
              justification: { type: string }
              alternatives: { type: string }
              timestamp: { type: string, format: date-time }
            required: [title, context, decision, justification]
          Progress:
            type: object
            properties:
              title: { type: string }
              status: { type: string }
              deliverables: { type: string }
              notes: { type: string } # Optional notes
              timestamp: { type: string, format: date-time }
            required: [title, status, deliverables]

        feedback:
          default:
            type: object
            properties:
              source: { type: string }
              issue: { type: string }
              analysis: { type: string }
              action: { type: string }
              timestamp: { type: string, format: date-time }
            required: [source, issue]

        maintenance:
          Maintenance Log:
            type: object
            properties:
              action: { type: string }
              description: { type: string }
              timestamp: { type: string, format: date-time }
            required: [action, description]
          Known Issues:
            type: object
            properties:
              issue_description: { type: string }
              status: { type: string, enum: ["Open", "Investigating", "Resolved"] }
              timestamp: { type: string, format: date-time }
            required: [issue_description, status]
          Structure Changes:
            type: object
            properties:
              change_description: { type: string }
              timestamp: { type: string, format: date-time }
            required: [change_description]
          Future Improvements:
            type: object
            properties:
              improvement_idea: { type: string }
              timestamp: { type: string, format: date-time }
            required: [improvement_idea]

        # --- Mode-Specific Schemas ---
        sparc:
          Delegations Log:
            type: object
            properties:
              task_name: { type: string }
              mode_slug: { type: string }
              description: { type: string }
              deliverable: { type: string }
              status: { type: string, enum: ["pending", "active", "completed", "blocked", "failed"] }
              completion_time: { type: string, format: date-time }
              outcome: { type: string }
              progress_link: { type: string }
              timestamp: { type: string, format: date-time }
            required: [task_name, mode_slug, description, deliverable, status]
          Workflow State:
            type: object
            properties:
              phase: { type: string }
              phase_start: { type: string, format: date-time }
              focus: { type: string }
              actions: { type: [string, array], items: { type: string } }
              timestamp: { type: string, format: date-time }
            required: [phase, focus, actions]

        tdd:
          Test Plans:
            type: object
            properties:
              title: { type: string }
              unit_tests:
                type: array
                items:
                  type: object
                  properties:
                    description: { type: string }
                    expected: { type: string }
                    status: { type: string, enum: ["Planned", "Written", "Passing", "Failing"] }
                  required: [description, expected, status]
              integration_tests:
                type: array
                items:
                  type: object
                  properties:
                    description: { type: string }
                    expected: { type: string }
                    status: { type: string, enum: ["Planned", "Written", "Passing", "Failing"] }
                  required: [description, expected, status]
              edge_cases:
                type: array
                items:
                  type: object # Assuming object format like {description: ..., test_approach: ...}
                  properties:
                    description: { type: string }
                    test_approach: { type: string }
                  required: [description]
              timestamp: { type: string, format: date-time }
            required: [title]
          Test Coverage Summary:
            type: object
            properties:
              line: { type: number }
              branch: { type: number }
              function: { type: number }
              components: { type: string } # Or object if more structured
              attention_areas: { type: string }
              timestamp: { type: string, format: date-time }
            required: [line, branch, function]
          # ... Add schemas for other tdd sections ...

        code:
          Implementation Notes:
            type: object
            properties:
              feature_component: { type: string }
              approach: { type: string }
              files: { type: [string, array], items: { type: string } }
              notes: { type: string }
              timestamp: { type: string, format: date-time }
            required: [feature_component, approach, files]
          Technical Debt Log:
            type: object
            properties:
              issue_name_id: { type: string }
              status: { type: string, enum: ["Open", "Investigating", "Resolved", "Deferred"] }
              identified_time: { type: string, format: date-time }
              location: { type: string }
              description: { type: string }
              impact: { type: string }
              priority: { type: string, enum: ["High", "Medium", "Low"] }
              solution: { type: string }
              resolution: { type: string }
              resolved_date: { type: string, format: date-time }
              timestamp: { type: string, format: date-time }
            required: [issue_name_id, status, location, description, priority]
          # ... Add schemas for other code sections ...

        # --- Other Modes ---
        # Add schemas for spec-pseudocode, architect, debug, security-review, etc.
        # based on their format definitions and .clinerules files.
        # Example for security-review:
        security-review:
          Security Findings Log:
            type: object
            properties:
              finding_id: { type: string }
              short_description: { type: string }
              status: { type: string, enum: ["Open", "Resolved", "Risk Accepted"] }
              severity: { type: string, enum: ["Critical", "High", "Medium", "Low", "Info"] }
              components: { type: [string, array], items: { type: string } }
              description: { type: string }
              owasp: { type: string }
              poc: { type: string }
              remediation: { type: string }
              resolved_time: { type: string, format: date-time }
              timestamp: { type: string, format: date-time }
            required: [finding_id, short_description, status, severity, components, description, remediation]
          # ... etc ...

        # ... Add other modes similarly ...
        ````

**Phase 3: Update Dependencies**

1.  **Goal:** Add necessary Python libraries.
2.  **Action:** Based on the `pyproject.toml` content you read earlier:
    *   If using Poetry: Add `PyYAML` and `jsonschema` under `[tool.poetry.dependencies]`.
        ```diff
        // filepath: pyproject.toml
        <<<<<<< SEARCH
        :start_line:X // Find the start of [tool.poetry.dependencies]
        :end_line:Y // Find the end of [tool.poetry.dependencies]
        -------
        [tool.poetry.dependencies]
        python = "^3.9"
        # ... other dependencies ...
        =======
        [tool.poetry.dependencies]
        python = "^3.9"
        # ... other dependencies ...
        PyYAML = "^6.0"
        jsonschema = "^4.17" # Or latest stable version
        >>>>>>> REPLACE
        ```
    *   If using requirements.txt: Add `PyYAML>=6.0` and `jsonschema>=4.17` to the file.
        ```diff
        // filepath: requirements.txt
        <<<<<<< SEARCH
        :start_line:1 // Assuming it's a simple list
        :end_line:Z // End of file
        -------
        # Existing requirements...
        =======
        # Existing requirements...
        PyYAML>=6.0
        jsonschema>=4.17
        >>>>>>> REPLACE
        ```
3.  **Instruction:** Inform the user that dependencies have been updated and they might need to run `poetry install` or `pip install -r requirements.txt`.

**Phase 4: Implement update_memory_bank.py**

1.  **Goal:** Refactor the script to use external formats, validate input using schemas, and handle section-based updates correctly.
2.  **Action:** Apply the following changes using `apply_diff` or `insert_content`. Be precise with line numbers and indentation.

    *   **Add Imports:**
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/update_memory_bank.py
        import argparse
        import json
        import os
        import re # Add
        import datetime # Add
        import yaml # Add
        from pathlib import Path
        import sys # Add
        from typing import Dict, List, Any, Optional, Union # Add
        from jsonschema import validate, ValidationError # Add

        # Add Global Variables for loaded configs
        MEMORY_FORMATS = {}
        MEMORY_SCHEMAS = {}
        ```
    *   **Add Config Loading Functions:**
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/update_memory_bank.py
        # Insert after imports

        def load_config_yaml(config_path: Path, config_name: str) -> Dict:
            """Loads a YAML configuration file."""
            if not config_path.is_file():
                print(f"❌ Error: {config_name} file not found at {config_path}", file=sys.stderr)
                sys.exit(1)
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f"❌ Error parsing {config_name} file {config_path}: {e}", file=sys.stderr)
                sys.exit(1)
            except Exception as e:
                print(f"❌ Error reading {config_name} file {config_path}: {e}", file=sys.stderr)
                sys.exit(1)

        # ... (Keep get_timestamp function) ...
        ```
    *   **Refactor `find_section`:** (Replace existing function)
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/update_memory_bank.py
        # Replace the old find_section_boundaries function

        def find_section(content: str, section_name: str) -> Optional[dict]:
            """
            Find a section in markdown content by name.
            Returns dict with start/end positions and level, or None if not found.
            """
            # Escape special regex characters in section_name
            escaped_name = re.escape(section_name)

            # Try to find the section heading at any markdown heading level (# to ######)
            for level in range(1, 7):
                # Match heading, allowing optional trailing whitespace
                heading_pattern = f"^( {'#' * level}\\s+{escaped_name}\\s* )$"
                match = re.search(heading_pattern, content, re.MULTILINE | re.VERBOSE)
                if match:
                    section_start = match.start()
                    section_level = level

                    # Find the next heading at same or higher level
                    # Look for lines starting with 1 to section_level '#' characters followed by space
                    next_heading_pattern = f"^#{{1,{section_level}}}\\s+"
                    # Search from the end of the current heading match
                    next_match = re.search(next_heading_pattern, content[match.end():], re.MULTILINE)

                    if next_match:
                        # Calculate end position relative to the original content string
                        section_end = match.end() + next_match.start()
                    else:
                        # No subsequent heading found, section goes to end of content
                        section_end = len(content)

                    return {
                        "start": section_start,
                        "end": section_end,
                        "level": section_level,
                        "name": section_name,
                        "heading": content[match.start():match.end()].strip() # Store the exact heading found
                    }

            return None
        ```
    *   **Refactor `update_section`:** (Replace existing function)
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/update_memory_bank.py
        # Replace the old update_section function

        def update_section(content: str, section_name: str, new_content: str, append: bool = True) -> str:
            """
            Update a section in markdown content. Creates section if not found.
            If append=True, appends the content within the section.
            Otherwise, replaces the content of the section (below the heading).
            Returns the updated content.
            """
            section = find_section(content, section_name)
            new_content = new_content.strip() # Ensure no leading/trailing whitespace in new content itself

            if section:
                # Section exists
                heading_end_pos = section["start"] + len(section["heading"])
                # Ensure there's a newline after the heading before content starts
                if not content[heading_end_pos:].startswith('\n'):
                     heading_end_pos = section["start"] + len(content[section["start"]:section["end"]].split('\n', 1)[0])


                # Content starts after the heading line and any immediate newline
                content_start_pos = heading_end_pos
                while content_start_pos < section["end"] and content[content_start_pos] == '\n':
                    content_start_pos += 1

                section_end_pos = section["end"]

                if append:
                    # Append within the section, before the next section starts
                    # Ensure separation with existing content and the new content
                    existing_section_content = content[content_start_pos:section_end_pos].rstrip()
                    separator = "\n\n" if existing_section_content else "" # Add blank line if content exists

                    # Insert before the section end position
                    updated_content = (content[:section_end_pos].rstrip() + # Content up to section end, remove trailing whitespace
                                       separator +
                                       new_content + "\n\n" + # Add new content with trailing blank line
                                       content[section_end_pos:]) # Content after the section
                else:
                    # Replace content within the section
                    # Ensure blank lines around the new content
                    updated_content = (content[:heading_end_pos] + # Keep the heading
                                       "\n\n" + new_content + "\n\n" + # Add new content with surrounding blank lines
                                       content[section_end_pos:]) # Keep content after the section
            else:
                # Section doesn't exist, add it to the end
                # Ensure separation from previous content
                separator = "\n\n" if content.strip() and not content.endswith('\n\n') else ""
                if content.strip() and not content.endswith('\n'):
                     separator = "\n\n" # Force double newline if content exists but doesn't end with newline

                # Default to heading level 2 (##)
                heading = f"## {section_name}"
                updated_content = content.rstrip() + separator + heading + "\n\n" + new_content + "\n\n"

            # Clean up potential multiple blank lines resulting from operations
            updated_content = re.sub(r'\n{3,}', '\n\n', updated_content).strip() + "\n" # Ensure single trailing newline
            return updated_content
        ```
    *   **Add Helper Functions:** (`ensure_file_exists`, `read_file_content`, `write_file_content`, `format_list_items`)
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/update_memory_bank.py
        # Insert before format_template_data

        def ensure_file_exists(file_path: Path, default_content: str = "") -> bool:
            """Ensure a file exists, creating it with default content if not."""
            if not file_path.exists():
                try:
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(default_content)
                    return True # Indicates file was created
                except Exception as e:
                    print(f"❌ Error creating file {file_path}: {e}", file=sys.stderr)
                    # Decide if this should be fatal
                    return False
            return False # File already existed

        def read_file_content(file_path: Path) -> str:
            """Reads content or returns empty string."""
            if file_path.is_file():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        return f.read()
                except Exception as e:
                    print(f"❌ Error reading file {file_path}: {e}", file=sys.stderr)
            return ""

        def write_file_content(file_path: Path, content: str) -> bool:
            """Writes content, returns success status."""
            try:
                # Ensure parent dir exists, necessary if ensure_file_exists wasn't called or failed
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
            except Exception as e:
                print(f"❌ Error writing file {file_path}: {e}", file=sys.stderr)
                return False

        def format_list_items(items: List[Any], item_template: str) -> str:
            """Formats a list of items using a template for each."""
            if not items:
                return "- None yet." # Or configure this default
            formatted_lines = []
            for item in items:
                if isinstance(item, dict):
                    try:
                        # Add timestamp to item if template expects it and it's missing
                        if '{timestamp}' in item_template and 'timestamp' not in item:
                            item['timestamp'] = get_timestamp()
                        formatted_lines.append(item_template.format(**item))
                    except KeyError as e:
                        print(f"⚠️ Warning: Missing key '{e}' formatting list item. Item: {item}", file=sys.stderr)
                        formatted_lines.append(f"- Error formatting item: {item}")
                    except Exception as e:
                         print(f"⚠️ Warning: Error formatting list item: {e}. Item: {item}", file=sys.stderr)
                         formatted_lines.append(f"- Error formatting item: {item}")
                else:
                    # Handle non-dict items if necessary, maybe just stringify
                     formatted_lines.append(f"- {str(item)}") # Basic fallback
            return "\n".join(formatted_lines)

        def get_schema(file_key: str, section_name: Optional[str] = None) -> Optional[Dict]:
            """Retrieves the validation schema."""
            if section_name:
                 # Look for specific section schema first
                 schema = MEMORY_SCHEMAS.get(file_key, {}).get(section_name)
                 if schema:
                     return schema
            # Fallback to default schema for the file type
            return MEMORY_SCHEMAS.get(file_key, {}).get("default")

        def get_format_template(file_key: str, section_name: Optional[str] = None) -> Optional[Union[str, Dict]]:
             """Retrieves the format template."""
             if section_name:
                 template = MEMORY_FORMATS.get(file_key, {}).get(section_name)
                 if template:
                     return template
             return MEMORY_FORMATS.get(file_key, {}).get("default")
        ```
    *   **Refactor `format_template_data`:** (Replace existing function)
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/update_memory_bank.py
        # Replace the old format_content function

        def format_template_data(file_key: str, section_name: Optional[str], data: dict) -> str:
            """Formats data using loaded templates."""
            if not isinstance(data, dict):
                 print(f"⚠️ Warning: Expected dict data for formatting, got {type(data)}. Stringifying.", file=sys.stderr)
                 return str(data) # Or handle error differently

            # Add timestamp if not present
            if 'timestamp' not in data:
                data['timestamp'] = get_timestamp()

            template = get_format_template(file_key, section_name)

            if not template:
                print(f"⚠️ Warning: No format template found for {file_key}/{section_name or 'default'}. Using basic YAML.", file=sys.stderr)
                try:
                    # Basic YAML dump as fallback
                    return f"```yaml\n{yaml.dump(data, default_flow_style=False, sort_keys=False)}\n```\n"
                except Exception as e:
                    print(f"❌ Error during fallback YAML formatting: {e}", file=sys.stderr)
                    return f"Formatting Error: {data}" # Last resort

            try:
                if isinstance(template, dict): # Handle structured templates (like Test Plans)
                    formatted_output = ""
                    if '_header' in template:
                        formatted_output += template['_header'].format(**data) + "\n"

                    # Process list items based on convention (e.g., 'unit_tests' maps to '_unit_test_item')
                    for key, value in data.items():
                        if isinstance(value, list):
                            item_template_key = f"_{key.replace('_', '')}_item" # e.g., unit_tests -> _unittestitem
                            # Try variations for flexibility
                            possible_item_keys = [f"_{key}_item", f"_{key.rstrip('s')}_item"]
                            item_template = None
                            for pk in possible_item_keys:
                                if pk in template:
                                    item_template = template[pk]
                                    break

                            if item_template:
                                # Add sub-heading based on key (e.g., "Unit Tests")
                                sub_heading = key.replace('_', ' ').title()
                                formatted_output += f"#### {sub_heading}:\n"
                                formatted_output += format_list_items(value, item_template) + "\n"
                            # else: # Optional: Warn if list data has no matching item template
                            #    print(f"⚠️ Warning: No item template found for list '{key}' in {file_key}/{section_name}", file=sys.stderr)

                    # Handle potential _content block
                    if '_content' in template and '_content' in data:
                         formatted_output += template['_content'].format(content=data['_content']) + "\n"

                    return formatted_output.strip()

                elif isinstance(template, str): # Simple string template
                    # Handle special cases like optional notes
                    if '{notes_section}' in template:
                         notes_content = f"- **Notes:** {data.get('notes', '')}\n" if data.get('notes') else ""
                         data['notes_section'] = notes_content # Inject for formatting

                    # Handle list actions
                    if '{actions}' in template and isinstance(data.get('actions'), list):
                         data['actions'] = "\n    - ".join(data['actions']) # Format as indented list items

                    return template.format(**data).strip()
                else:
                     raise TypeError(f"Unexpected template type: {type(template)}")

            except KeyError as e:
                print(f"❌ Formatting Error: Missing key '{e}' for template {file_key}/{section_name or 'default'}.", file=sys.stderr)
                print(f"   Provided data keys: {list(data.keys())}", file=sys.stderr)
                # Optionally list expected keys from template string
                if isinstance(template, str):
                     expected_keys = re.findall(r'\{(\w+)\}', template)
                     print(f"   Template expects: {expected_keys}", file=sys.stderr)
                return f"Formatting Error - Missing Key: {e}" # Return error string
            except Exception as e:
                print(f"❌ Unexpected Formatting Error for {file_key}/{section_name or 'default'}: {e}", file=sys.stderr)
                return f"Unexpected Formatting Error: {e}" # Return error string

        ```
    *   **Refactor Main Update Functions:** (Replace `update_active_context`, `update_global_context`, etc. with validated versions)
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/update_memory_bank.py
        # Replace old update functions (update_active_context, update_global_context, etc.)

        def update_memory_file(file_path: Path, file_key: str, default_content: str,
                               data: Union[Dict, str], section_name: Optional[str] = None,
                               append: bool = True) -> dict:
            """Generic function to update a memory bank file with validation."""
            result = {"file": file_path.name, "section": section_name, "success": False, "message": ""}

            # 1. Ensure file exists
            created = ensure_file_exists(file_path, default_content)
            content = read_file_content(file_path)
            if not content and not created: # Read failed but file should exist
                 result["message"] = f"Failed to read existing file {file_path}"
                 return result
            if not content and created:
                 content = default_content # Use default if newly created

            # 2. Handle non-structured (string) data - bypass validation/formatting
            if isinstance(data, str):
                formatted_data = data # Use raw string
                if section_name:
                    updated_content = update_section(content, section_name, formatted_data, append)
                else: # Update whole file
                    if append:
                        updated_content = content.rstrip() + "\n\n" + formatted_data + "\n"
                    else:
                        # Try to preserve header if overwriting whole file
                        header_match = re.match(r'^(#[^\n]+(?:\n{1,2}|$))', content, re.MULTILINE)
                        header = header_match.group(1) if header_match else default_content.split('\n\n', 1)[0] + "\n\n"
                        updated_content = header + formatted_data + "\n"
            # 3. Handle structured (dict) data - validate and format
            elif isinstance(data, dict):
                # 3a. Validate Input Data
                schema = get_schema(file_key, section_name)
                if schema:
                    try:
                        validate(instance=data, schema=schema)
                    except ValidationError as e:
                        result["message"] = f"JSON Validation Error for {file_key}/{section_name or 'default'}: {e.message}. Path: {list(e.path)}. Schema snippet: {e.schema}"
                        # Provide more context if possible
                        if e.instance:
                             result["message"] += f". Instance: {str(e.instance)[:100]}..." # Show part of failing data
                        return result # Validation failed
                # else: # Optional: Warn if no schema found for validation
                #    print(f"⚠️ Warning: No validation schema found for {file_key}/{section_name or 'default'}", file=sys.stderr)

                # 3b. Format Data
                formatted_data = format_template_data(file_key, section_name, data)
                if "Formatting Error" in formatted_data: # Check if formatting failed
                    result["message"] = formatted_data
                    return result # Formatting failed

                # 3c. Update Content
                if section_name:
                    updated_content = update_section(content, section_name, formatted_data, append)
                else: # Update whole file (rare for structured data unless replacing)
                     if append:
                         updated_content = content.rstrip() + "\n\n" + formatted_data + "\n"
                     else:
                         # Preserve header
                         header_match = re.match(r'^(#[^\n]+(?:\n{1,2}|$))', content, re.MULTILINE)
                         header = header_match.group(1) if header_match else default_content.split('\n\n', 1)[0] + "\n\n"
                         updated_content = header + formatted_data + "\n"
            else:
                 result["message"] = f"Invalid data type for update: {type(data)}"
                 return result

            # 4. Write Updated Content
            if write_file_content(file_path, updated_content):
                result["success"] = True
                result["message"] = f"{'Appended to' if append else 'Updated'} section '{section_name or 'file'}' in {file_path}"
                if created:
                    result["message"] += " (File created)"
            else:
                result["message"] = f"Failed to write updated content to {file_path}"

            return result
        ```
    *   **Refactor `main()`:** (Replace existing `main` function)
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/update_memory_bank.py
        # Replace the old main function

        def main():
            global MEMORY_FORMATS, MEMORY_SCHEMAS # Allow modification of globals

            parser = argparse.ArgumentParser(description="Update memory bank files with structured, validated data.")
            parser.add_argument("--mode-slug", required=True, help="The slug of the mode performing the update.")
            parser.add_argument("--memory-path", default="memory-bank", help="Path to the memory bank directory.")
            # Arguments now expect JSON string or file path
            parser.add_argument("--active-context", help="JSON string/file path for activeContext.md update (single entry).")
            parser.add_argument("--global-context", help="JSON string/file path for globalContext.md updates (object with section names as keys).")
            parser.add_argument("--mode-specific", help="JSON string/file path for mode-specific updates (object with section names as keys).")
            parser.add_argument("--feedback", help="JSON string/file path for feedback update (single entry).")
            parser.add_argument("--maintenance", help="JSON string/file path for maintenance.md updates (object with section names as keys).")
            parser.add_argument("--append", action="store_true", help="Append entries within sections instead of replacing section content.")
            parser.add_argument("--commit", action="store_true", help="Commit changes to git (requires version_control.py).")
            args = parser.parse_args()

            memory_base_path = Path(args.memory_path)
            mode_slug = args.mode_slug
            results = []

            # --- Load Configurations ---
            script_dir = Path(__file__).parent.parent # .roo directory
            config_dir = script_dir / "config"
            MEMORY_FORMATS = load_config_yaml(config_dir / "memory_formats.yaml", "Memory Formats")
            MEMORY_SCHEMAS = load_config_yaml(config_dir / "memory_schemas.yaml", "Memory Schemas")
            # --- End Load Configurations ---

            if not memory_base_path.is_dir():
                print(f"❌ Error: Memory bank directory not found at '{memory_base_path}'", file=sys.stderr)
                return 1

            # Helper function to parse JSON input (string or file)
            def parse_json_input(input_str: Optional[str]) -> Optional[Union[Dict, List, str]]:
                if not input_str: return None
                path = Path(input_str)
                if path.is_file():
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            return json.load(f)
                    except json.JSONDecodeError as e:
                        print(f"❌ Error parsing JSON file {path}: {e}", file=sys.stderr)
                        return None # Or raise/exit
                    except Exception as e:
                         print(f"❌ Error reading file {path}: {e}", file=sys.stderr)
                         return None
                else:
                    try:
                        return json.loads(input_str)
                    except json.JSONDecodeError:
                        # If not valid JSON and not a file, treat as raw string? Or error?
                        # Let's error for now, assuming structured input is intended
                        print(f"❌ Error: Input is not valid JSON and not a readable file path: {input_str[:100]}...", file=sys.stderr)
                        return None # Or raise/exit

            # --- Process Updates ---
            if args.active_context:
                data = parse_json_input(args.active_context)
                if data:
                    # Active context is usually a single entry prepended/replaced
                    results.append(update_memory_file(
                        memory_base_path / "activeContext.md", "active_context",
                        "# Active Context\n\n", data, section_name=None, append=args.append
                    ))

            if args.global_context:
                data = parse_json_input(args.global_context)
                if isinstance(data, dict):
                    for section, section_data in data.items():
                        results.append(update_memory_file(
                            memory_base_path / "globalContext.md", "global_context",
                            "# Global Context\n\n", section_data, section_name=section, append=args.append
                        ))
                elif data is not None:
                     print("❌ Error: --global-context requires a JSON object (dict) input.", file=sys.stderr)

            if args.mode_specific:
                data = parse_json_input(args.mode_specific)
                if isinstance(data, dict):
                     mode_file_path = memory_base_path / "mode-specific" / f"{mode_slug}.md"
                     default_content = f"# {mode_slug.capitalize()} Specific Memory\n\n"
                     for section, section_data in data.items():
                         results.append(update_memory_file(
                             mode_file_path, mode_slug, default_content,
                             section_data, section_name=section, append=args.append
                         ))
                elif data is not None:
                     print(f"❌ Error: --mode-specific requires a JSON object (dict) input for mode '{mode_slug}'.", file=sys.stderr)


            if args.feedback:
                data = parse_json_input(args.feedback)
                if data:
                    feedback_file_path = memory_base_path / "feedback" / f"{mode_slug}-feedback.md"
                    default_content = f"# {mode_slug.capitalize()} Feedback\n\n"
                    # Feedback is typically appended as distinct entries
                    results.append(update_memory_file(
                        feedback_file_path, "feedback", default_content,
                        data, section_name=None, append=True # Always append feedback entries
                    ))

            if args.maintenance:
                 data = parse_json_input(args.maintenance)
                 if isinstance(data, dict):
                     maint_file_path = memory_base_path / "maintenance.md"
                     default_content = "# Memory Bank Maintenance\n\n## Maintenance Log\n| Date | Action | Description |\n|------|--------|-------------|\n\n## Known Issues\n\n## Structure Changes\n\n## Future Improvements\n\n"
                     for section, section_data in data.items():
                         # Special handling for Maintenance Log table might be needed here
                         # For now, treat like other sections
                         results.append(update_memory_file(
                             maint_file_path, "maintenance", default_content,
                             section_data, section_name=section, append=args.append
                         ))
                 elif data is not None:
                     print("❌ Error: --maintenance requires a JSON object (dict) input.", file=sys.stderr)

            # --- Print Results ---
            success_count = 0
            for result in results:
                status = "✅" if result.get("success", False) else "❌"
                print(f"{status} {result.get('message', 'Unknown error')}")
                if result.get("success", False):
                    success_count += 1

            # --- Commit Changes ---
            if args.commit and success_count > 0:
                script_dir = Path(__file__).parent
                version_control_script = script_dir / "version_control.py"
                if version_control_script.exists():
                    commit_message = f"docs: {'Append to' if args.append else 'Update'} memory bank via {mode_slug}"
                    try:
                        # Use subprocess to call the version control script
                        process = subprocess.run(
                            [sys.executable, str(version_control_script), "commit",
                             "--message", commit_message,
                             "--paths", str(memory_base_path), # Commit only memory bank changes
                             "--semantic-prefix", "docs", # Use 'docs' for memory bank changes
                             "--skip-tests"], # Don't run project tests for memory bank commit
                            capture_output=True, text=True, check=False, cwd=script_dir.parent.parent # Run from project root
                        )
                        if process.returncode == 0:
                            print(f"✅ Git commit successful.")
                            # print(process.stdout) # Optional: show commit output
                        else:
                            print(f"❌ Git commit failed. Exit code: {process.returncode}", file=sys.stderr)
                            print(f"   Error: {process.stderr}", file=sys.stderr)
                    except Exception as e:
                        print(f"❌ Failed to execute version_control.py: {e}", file=sys.stderr)
                else:
                    print("⚠️ Warning: version_control.py not found, skipping commit.", file=sys.stderr)

            # Exit with non-zero status if any update failed
            if results and success_count < len(results):
                 return 1
            elif not results:
                 print("ℹ️ No update arguments provided.")
                 return 0 # No work done is not an error
            else:
                 return 0 # All updates succeeded
        ```

**Phase 5: Implement read_memory_bank.py**

1.  **Goal:** Update the script to support section extraction and multiple output formats.
2.  **Action:** Apply the following changes using `apply_diff` or `insert_content`.

    *   **Add Imports:**
        ```python
        // filepath: /home/rookslog/zlibrary-mcp/.roo/scripts/read_memory_bank.py
        import argparse
        import os
        import re # Add
        import json # Add
        import yaml # Add
        from pathlib import Path
        import sys # Add
        from typing import Dict, List, Any, Optional # Add
        ```
    *   **Add/Refactor Helper Functions:** (`extract_section`, `extract_sections`, `format_file_content`, `get_memory_files`, `read_memory_as_text`, `read_memory_as_json`) - Use the versions from the previous plan. Insert these before `main`.
    *   **Refactor `main()`:** (Replace existing `main` function) - Use the version from the previous plan which includes argument parsing for format, section, etc., and calls the new reading functions.

**Phase 6: Refine `version_control.py`**

1.  **Goal:** Make the script more robust and add the `status` command.
2.  **Action:** Apply the following changes using `apply_diff` or `insert_content`.

    *   **Add Imports:** `typing`.
    *   **Add/Refactor Helper Functions:** (`run_command`, `get_repository_info`, `run_tests`) - Use versions from the previous plan.
    *   **Refactor Core Functions:** (`commit_changes`, `create_branch`, `switch_branch`, `create_tag`, `complete_feature`) - Use versions from the previous plan.
    *   **Refactor `main()`:** (Replace existing `main` function) - Use the version from the previous plan which includes updated argument parsing and logic for all commands, including `status`.

**Phase 7: Update `.clinerules` Files**

1.  **Goal:** Remove specific format definitions and add guidance on required JSON fields.
2.  **Action:** For *each* `.clinerules-*.{yaml,markdown}` file you read initially (and others like `architect`, `spec-pseudocode`, etc.):
    *   Use `<read_file>` to get the current content.
    *   Identify lines defining specific formats (e.g., `delegations_log_format: |`, `test_plans_format: |`).
    *   Use `<apply_diff>` to **remove** these format definition blocks entirely.
    *   Within the `update_process:` or `mode_specific_updates:` sections, **add** comments or instructions mentioning the expected JSON structure and required fields for common updates, referencing `memory_schemas.yaml`.
    *   **Example Diff for .clinerules-tdd:**
        ```diff
        // filepath: /home/rookslog/zlibrary-mcp/.roo/rules-tdd/.clinerules-tdd
        <<<<<<< SEARCH
        :start_line:X // Line where test_plans_format starts
        :end_line:Y // Line where test_plans_format ends
        -------
            test_plans_format: |
              ### Test Plan: [Component/Feature] - [YYYY-MM-DD HH:MM:SS]
              #### Unit Tests: - Test Case: [desc] / Expected: [behavior] / Status: [Planned|Written|Passing|Failing]
              #### Integration Tests: - Test Case: [desc] / Expected: [behavior] / Status: [Planned|Written|Passing|Failing]
              #### Edge Cases Covered: - [edge case]: [test approach]
        =======
        >>>>>>> REPLACE
        // Remove other format definitions similarly (coverage_format, etc.)

        <<<<<<< SEARCH
        :start_line:Z // Line within update_process or mode_specific_updates
        :end_line:Z
        -------
              ## Test Plans (Driving Implementation)
              <!-- Append new test plans using the format below -->
        =======
              ## Test Plans (Driving Implementation)
              <!-- Append new test plans using update_memory_bank.py with JSON matching the 'tdd/Test Plans' schema in memory_schemas.yaml. Required fields: title, unit_tests (list of objects with description, expected, status). -->
        >>>>>>> REPLACE
        // Add similar comments for other sections like Test Coverage Summary etc.
        ```
    *   Repeat this process carefully for all relevant `.clinerules` files.

**Phase 8: Finalization**

1.  **Goal:** Ensure the system is ready.
2.  **Action:** Inform the user: "Implementation complete. Dependencies (`PyYAML`, `jsonschema`) added. Please run your dependency manager (`poetry install` or `pip install -r requirements.txt`). The memory bank system now uses external configuration for formats and schemas, includes input validation, and offers more robust section-based updates."
3.  **Action (Optional):** Suggest committing the changes using the newly updated script:
    `<run_command><command>python .roo/scripts/version_control.py commit --semantic-prefix feat --message "Implement enhanced memory bank system with validation"</command></run_command>`

This detailed plan provides the necessary steps, including file reading, creation, and specific modifications using diffs where possible, for the AI Coding Agent to implement the enhanced memory bank system. Remember to be careful with line numbers and indentation when applying changes.