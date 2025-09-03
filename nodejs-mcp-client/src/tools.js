/**
 * Tools definitions for FORMS Edge Delivery MCP Server
 */

/**
 * Get available tools
 * @returns {Array} Array of tool definitions
 */
export function getTools() {
  return [
    {
      name: 'get_field_structure_styling',
      description: 'Get field structure styling and markup patterns for Adaptive Form Block. Returns HTML structure and CSS for form fields including labels, inputs, wrappers, and validation states.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_dropdown_styling',
      description: 'Get dropdown component styling for Adaptive Form Block. Returns CSS and HTML patterns for dropdown elements including select boxes, option styling, and custom dropdown implementations.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_radio_checkbox_styling',
      description: 'Get radio button and checkbox styling for Adaptive Form Block. Returns CSS and HTML patterns for radio buttons, checkboxes, groups, and custom styled form controls.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_panel_container_styling',
      description: 'Get panel and container styling for Adaptive Form Block. Returns CSS and HTML patterns for form panels, fieldsets, containers, and layout structures.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_css_selectors_guide',
      description: 'Get comprehensive CSS selectors guide for Adaptive Form Block. Returns a complete guide to CSS selectors for form styling and customization.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_file_attachment_styling',
      description: 'Get file attachment component styling for Adaptive Form Block. Returns CSS and HTML for file upload elements, drag-and-drop zones, and custom file input styling.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_error_message_styling',
      description: 'Get error message styling for Adaptive Form Block. Returns CSS and HTML for form validation errors, error states, and accessibility patterns.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_repeatable_panel_styling',
      description: 'Get repeatable panel styling for Adaptive Form Block. Returns CSS and HTML for dynamic repeatable form sections, including add/remove controls and layout.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_custom_component_creation',
      description: 'Get complete documentation for creating custom components (decorating fields) in Adaptive Form Block. Returns guide with decorator functions, custom styling, and behavior implementation.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_layout_configuration',
      description: 'Get complete documentation for panel layout configuration in Adaptive Form Block. Returns guide for implementing custom layouts like accordion, wizard, tabs, etc.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    },
    {
      name: 'get_system_information',
      description: 'Get system information and server details for Adaptive Form Block. Returns system details and environment info.',
      inputSchema: {
        type: 'object',
        properties: {},
        required: []
      }
    }
  ];
}

export default getTools;
