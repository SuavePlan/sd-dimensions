import gradio as gr

# Default dimensions pre-filled in the text box
default_dimensions = "SD 1.0:512x512;SD 2.0:768x768;SDXL 1.0:1024X1024,1408x704,1728x576"

def get_custom_dimensions():
    # Parse the input string to extract dimensions for each SD version
    dimensions_dict = {}
    for segment in default_dimensions.split(";"):
        version, dimensions = segment.split(":")
        dimensions_dict[version.strip()] = dimensions.split(",")
    
    return dimensions_dict

# Retrieve custom dimensions
custom_dimensions = get_custom_dimensions()

# Extract SD versions dynamically from the custom dimensions
sd_versions = list(custom_dimensions.keys())

# Set a default SD version and provide the corresponding dimensions as choices
default_sd_version = sd_versions[0]
default_choices = custom_dimensions[default_sd_version]

# Gradio interface
interface = gr.Interface(
    fn=lambda sd_version, dimensions: f"Selected SD Version: {sd_version}, Dimensions: {dimensions}",  # Just returning the selected values for demonstration
    inputs=[
        gr.components.Radio(sd_versions, label="Select SD Version"),
        gr.components.Dropdown(choices=default_choices, label="Select Dimensions")
    ],
    outputs="text",
    live=True
)

# Launch the Gradio interface
interface.launch()
