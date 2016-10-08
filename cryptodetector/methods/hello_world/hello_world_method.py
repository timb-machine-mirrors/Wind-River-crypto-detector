"""
/* <legal-notice>
*
* Copyright (c) 2016 Wind River Systems, Inc.
*
* This software has been developed and maintained under the Wind River
* CodeSwap program. The right to copy, distribute, modify, or otherwise
* make use of this software may be licensed only pursuant to the terms
* of an applicable Wind River license agreement.
*
* <credits>
*   { Kamyar Kaviani,  kamyar.kaviani@windriver.com}
* </credits>
*
* </legal-notice>
*/
"""

import re
from cryptodetector import Method, Languages

class HelloWorldScanner(Method):
    """Hello, World template method
    """

    method_id = "hello_world"

    # options={
    #     "example_value": 123,
    #     "example_array": [],
    #     "example_boolean": False
    # }

    # These help messages will be printed when the user brings up the help guide with -h

    # options_help = {
    #     "example_value": "This is an example help message describing example_value",
    #     "example_array": "This is an example help message describing example_array",
    #     "example_boolean": "This is an example help message describing example_boolean"
    # }

    def supports_scanning_file(self, language):
        """This method supports scanning all text files

        Args:
            language: (string) see langauges.py

        Returns:
            (bool) whether it supports scanning a file in the given language
        """
        return Languages.is_text(language)

    def quick_search(self, content, language):
        """Quickly search the content for the string "Hello, World"

        Args:
            content: (string) the file content in which to search
            language: (string) see langauges.py

        Returns:
            (bool) whether it found a match anywhere in the content
        """
        return "Hello, World" in content

    def search(self, content, language):
        """Search all occurances of the string "Hello, World"

        Args:
            content: (string) the file content in which to search
            language: (string) see langauges.py

        Returns:
            (list) list of matches. A match is a dict object containing the output fields
        """
        result = []

        for match in re.finditer("Hello, World", language):

            result.append({"match_type": "generic", \
                           "match_text": "Hello, World", \
                           "match_file_index_begin": match.start(), \
                           "match_file_index_end": match.end()})

        return result