/**
 * Prompts definitions for FORMS Edge Delivery MCP Server
 */

/**
 * Get available prompts
 * @returns {Array} Array of prompt definitions
 */
export function getPrompts() {
  return [
    {
      name: 'get_css_selectors_guide',
      description: 'Get the CSS selectors guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to master CSS selectors for targeting specific form elements in AEM Adaptive Forms. Show me advanced selector techniques for different field types, name-based targeting, and type-based selectors to create precise styling rules.'
    },
    {
      name: 'get_dropdown_styling',
      description: 'Get the dropdown styling guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to style dropdown components with modern visual effects. I want custom arrow styling, hover states, focus indicators, and smooth transition effects that work well with AEM Adaptive Form Block structure.'
    },
    {
      name: 'get_radio_checkbox_styling',
      description: 'Get the radio checkbox styling guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to create custom-styled radio buttons and checkboxes that replace the default browser appearance. Show me CSS techniques for creating modern, accessible radio groups and checkbox styling with custom indicators.'
    },
    {
      name: 'error_state_visual_design',
      description: 'Get the error state visual design guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to design comprehensive error styling for form validation. I need CSS for error message appearance, field border changes, icon integration, and smooth animation transitions between valid and error states.'
    },
    {
      name: 'get_panel_container_styling',
      description: 'Get the panel container styling guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to style panel containers and fieldsets for better visual hierarchy. I need CSS approaches for grouping elements, creating visual separation, and styling container borders and backgrounds.'
    },
    {
      name: 'get_layout_configuration',
      description: 'Get the layout configuration guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to implement sophisticated layout styling for wizard, accordion, and tab layouts. Show me CSS techniques for creating smooth transitions, step indicators, and responsive layout patterns.'
    },
    {
      name: 'get_error_message_styling',
      description: 'Get the error message styling guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to design comprehensive error styling for form validation. I need CSS for error message appearance, field border changes, icon integration, and smooth animation transitions between valid and error states.'
    },
    {
      name: 'file_upload_styling_enhancement',
      description: 'Get the Style of file upload components with drag-and-drop feedback.',
      arguments: [],
      prompt: 'I want to style file upload components with drag-and-drop visual feedback. Show me CSS techniques for upload area styling, drag states, progress indicators, and file preview styling.'
    },
    {
      name: 'panel_organization_container_styling',
      description: 'Get the panel organization and container styling guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'Help me style panel containers and fieldsets for better visual hierarchy. I need CSS approaches for grouping elements, creating visual separation, and styling container borders and backgrounds.'
    },
    {
      name: 'repeatable_dynamic_panel_animation_styling',
      description: 'Get the repeatable dynamic panel animation styling guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to style repeatable panels with smooth add/remove animations. Show me CSS techniques for animating panel appearance, styling control buttons, and creating seamless transitions for dynamic content.'
    },
    {
      name: 'custom_component_decorator_styling',
      description: 'Get the custom component decorator styling guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to create custom components decorators for form components with advanced styling. I want to understand CSS approaches for custom component styling, decorator implementation, and creating reusable styled components.'
    },
    {
      name: 'advanced_layout_styling_patterns',
      description: 'Get the advanced layout styling patterns guide for AEM Adaptive Form Block development like wizard, accordion, tabs on top, tabs on left etc.',
      arguments: [],
      prompt: 'I need to implement sophisticated layout patterns like wizard, accordion, tabs on top, tabs on left etc. Show me CSS techniques for creating smooth transitions, step indicators, and responsive layout patterns.'
    },
    {
      name: 'complete_form_theming_strategy',
      description: 'Get the complete form theming strategy guide for AEM Adaptive Form Block development.',
      arguments: [],
      prompt: 'I need to develop a comprehensive theming strategy for my entire form. I need CSS approaches that combine field styling, error states, interactive components, and layout patterns into a cohesive design system.'
    }
  ];
}

export default getPrompts;
