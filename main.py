import core
import sys
import json
import datetime
import logging

AVAILABLE_FLOWS = {
    "new": {
        "arguments": [
            "project_name"
        ],
        "processor": core.Project
    },
    "post": {
        "arguments": [
            "post_name",
            "post_category",
            "project_name"
        ],
        "processor": core.Post
    }
}
MINIMUM_COMMAND_LINE_ARGS = 1
FLOW_POSITION = 1
SCRIPT_NAME = 1

USAGE_SUMMARY = """
How to use ->
python3 main.py <COMMAND> <COMMAND_ARGUMENTS>
Create a new project: python3 main.py new <PROJECT_NAME>
Create a new blog post: python3 main.py post <POST_NAME> <PROJECT_NAME> <POST_CATEGORY>
"""

def exit_program():
    invalid_arguments_message = """
    Invalid amount of arguments, please try again with: \n {usage_summary}
    """
    invalid_arguments_message = invalid_arguments_message.format(
        usage_summary=USAGE_SUMMARY
    )
    logging.info(invalid_arguments_message)
    sys.exit(1)

def handler(user_input):
    if (len(user_input) -SCRIPT_NAME < MINIMUM_COMMAND_LINE_ARGS or 
            not AVAILABLE_FLOWS.get(user_input[FLOW_POSITION])):
        exit_program()

    if len(user_input) -SCRIPT_NAME != len(AVAILABLE_FLOWS.get(user_input[FLOW_POSITION])):
        exit_program()

    flow = AVAILABLE_FLOWS[user_input[FLOW_POSITION]]
    for index, required_argument in enumerate(flow['arguments']):
        if not user_input[index + (FLOW_POSITION + SCRIPT_NAME)].strip():
            exit_program()

    processor = flow['processor']
    processor(user_input[(FLOW_POSITION + SCRIPT_NAME): ])

if __name__ == "__main__":
    handler(sys.argv)