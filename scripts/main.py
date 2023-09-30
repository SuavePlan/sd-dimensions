import gradio as gr

# Default dimensions pre-filled in the text box
default_dimensions = "SD 1.0:512x512;SD 2.0:768x768;SDXL 1.0:1024x1024,1408x704,1728x576"

def get_custom_dimensions():
    # Retrieve the custom dimensions from the config
    dimensions_str = shared.opts.get("custom_dimensions", default_dimensions)
    
    # Parse the input string to extract dimensions for each SD version
    dimensions_dict = {}
    for segment in dimensions_str.split(";"):
        version, dimensions = segment.split(":")
        dimensions_dict[version.strip()] = dimensions.split(",")
    
    return dimensions_dict

# Retrieve custom dimensions
custom_dimensions = get_custom_dimensions()

# Extract SD versions dynamically from the custom dimensions
sd_versions = list(custom_dimensions.keys())

# Gradio interface
interface = gr.Interface(
    fn=lambda sd_version, dimensions: f"Selected SD Version: {sd_version}, Dimensions: {dimensions}",  # Just returning the selected values for demonstration
    inputs=[
        gr.inputs.Radio(sd_versions, label="Select SD Version"),
        gr.inputs.Dropdown(choices=lambda choice: custom_dimensions[choice], label="Select Dimensions")
    ],
    outputs="text",
    live=True
)

# Add a text box to the config for custom dimensions
def on_ui_settings():
    shared.opts.add_option("custom_dimensions", shared.OptionInfo(default_dimensions, "Specify dimensions for each SD version", section=("dimensions", "Dimensions")))

script_callbacks.on_ui_settings(on_ui_settings)

# Launch the Gradio interface
interface.launch()
