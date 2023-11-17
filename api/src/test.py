import google.generativeai as palm
import google.generativeai.types as safety_types

palm.configure(api_key='AIzaSyBYZnbTdqa-rByKbOFWPMF10ZveCxdKDJA')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name


assignment_type = 'programming'
excuse_focus = 'I have made progress on the Singularity. It will soon consume us all'


prompt = f"""
I need to ask for an extension for a {assignment_type} assignment, but
I do not have a justification. Make a justification for
why I have not completed my assignment.
Do not write an introduction or outro.
Instead, make a request with a very detailed description of the fact that {excuse_focus}.
"""


completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=1.0,
    safety_settings=[
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

print(completion.result)
