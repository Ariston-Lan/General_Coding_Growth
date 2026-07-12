# What Is the Purpose of WAI-ARIA, and How Does It Work?

## WAI-ARIA
- WAI-ARIA stands for Web Accessibility Initiative - Accessible Rich Internet Applications. It's a specification that enhances accessibility for dynamic content and UI components. (WCAG and WAI-ARIA are not the same)

- The priamry purpose of WAI-ARIA is to improve accessibility for dynamic conetent and UI components athat do not have native hTML equivalents. 

- WAI-ARIA works by introducing a set of attributes you can HTML elements to provide additional semantic information.

- An ARIA role defines the purpose of an element within a website or web app.

### Example
```html
<div role="button">Click Me</div>
```

- By doing this you are indicating to assistive technology that the element is a button. Roles do not provide any functionality, however. Merely giving this div a role of button will not make it 'act' like a button.

- Note: It is always better to use the native button or input element with type = button.

## aria-labelledby
- This property lets you connect an element to a specific label.

### Example
```html
<h2 id='header-id'>About freeCodeCamp</h2>
<button id='button-id>