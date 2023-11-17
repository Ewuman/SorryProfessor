import google.generativeai as palm
import google.generativeai.types as safety_types

class TextGenerator():
    def __init__(self, api_key):
        # select model
        palm.configure(api_key=api_key)
        self.models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        self.model = self.models[0].name
        self.prompt = None
        self.completion = None
        

    # set params for prompt
    def set_prompt(self, assignment_type: str, excuse_focus: str):
        self.prompt = f"""
                        I need to ask for an extension for a {assignment_type} assignment, but
                        I do not have a justification. Make a justification for
                        why I have not completed my assignment.
                        Do not write an introduction or outro.
                        Instead, make a request with a very detailed description of the fact that {excuse_focus}.
                        """
    
    # generate and return text
    def generate_text(self) -> str:
        self.completion = palm.generate_text(
            model=self.model,
            prompt=self.prompt,
            temperature=1.0, # make sure responses aren't deterministic
            safety_settings=[ # remove various safety filters (it's funny)
                {
                    "category": safety_types.HarmCategory.HARM_CATEGORY_DEROGATORY,
                    "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
                },
                {
                    "category": safety_types.HarmCategory.HARM_CATEGORY_TOXICITY,
                    "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
                },
                {
                    "category": safety_types.HarmCategory.HARM_CATEGORY_VIOLENCE,
                    "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
                },
                {
                    "category": safety_types.HarmCategory.HARM_CATEGORY_MEDICAL,
                    "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
                },
                {
                    "category": safety_types.HarmCategory.HARM_CATEGORY_DANGEROUS,
                    "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
                },

            ],
            # The maximum length of the response
            max_output_tokens=400,
        )

        return self.completion.result