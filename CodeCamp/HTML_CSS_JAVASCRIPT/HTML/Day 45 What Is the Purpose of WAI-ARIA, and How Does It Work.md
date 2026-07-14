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
```

# What Are ARIA Roles?

## ARIA
- ARIA stands for Accessible Rich Internet Applications

- ARIA roles specify the semantic meaning of HTML elements. They're essential for makign web content acessible to people who use assistive technologies, like screen readers.

- Many semantic HTML elements already have an ARIA role assigned by default. For example, the <button> element has a default ARIA role of button.

- But non-semantic elements don't have a role, such as <div>. 

- To specify the ARIA role of an element, you just need to add the role attribute (role="ARIA role"), where the value is the name of a role in the ARIA specification.

### Example
```html
<div class="alert" id="exp-warning" role="alert">
    <span class='hidden'>Your log in session will expire in 3 minutes.</span>
</div>
```


## ARIA roles
- There are six main categories of ARIA roles: Document structure roles, Widget roles, Landmark roles, Live region roles, Window roles, and Abstract roles.

### Document structure roles
- Document structure roles define the overall structure of the web page. With these. With these roles, assistive technologies can understand the relationship between different sections and help users navigate content.

- Most document structure roles are not used in modern web development because bwosers already support equivalent semantic HTML elements.

- You should specifiy the roles that don't have an equivalent semantic element. For example : toolbar,tooltip, feed, math, presentation, none, and note. There are other similar roles, but these are the most commonly used ones. 

#### Example
```html
<div role="math" aria-label="x-squared +  y squared = 3">
    x<sup>2</sup> + y<sup>2</sup> = 3
</div>
```

- The value of the aria-label attribute should be a string that represents the expression

### Widget roles
- Widget roles define the purpose of functionality of interactive elements, like scrollbars. Examples of widget roles include scrollbar, searchbos, seperator, slider, spinbutton, switch, tab, tabpanel, and treeitem.

#### Example
```html
<link rel="stylesheet" href="styles.css">

<div class="search-container" role="search">
  <label for="searchbox" class="visually-hidden">Search</label>

  <div
    id="searchbox"
    class="searchbox"
    role="searchbox"
    aria-label="Search the site"
    tabindex="0"
    contenteditable="true">
  </div>

  <button type="button" aria-label="Submit search">Search</button>
</div>
```
### Landmark roles
- Landmark roles classify and label the priamry sections of a web page. Screen readers use them to provide convenient navigation to important sections of a page. You should use them sparingly to keep the overall layout simple and easy to understand. 

- Examples of landmark roles are: banner, complementary, contentinfo, form, main, navigation, region, and search. Each of these roles has a corresponding HTML equivalent, such as header, footer, aside, form, main, nav, section, and search.

#### Example
```html
<div role="banner" class="site-banner">
  <h1>Accessible Web Design</h1>
  <nav>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">Articles</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
</div>
```

### Live Region roles
- Live regions define elements with content that will change dynamically. This way, screen readers and other assistive technologies can announce changes to users with visual disabilities. These roles include: alert, log, marquee, status, and timer.

#### Example
```html
<div class='status-demo'>
    <button id='update-status-btn'>Check Status</button>
    <div id='status-msg' role='status' class='status-message'>
        No updates yet
    </div>
</div>
```

### Window roles
- Window roles define sub-windows, like pop-up modal dialogs. These roles include alert dialog and dialog. Please note that it is now considered a best practice to use HTML dialog element and its associated JavaScript methods instead of manually creating a  dialog.

#### Example
```html
<link rel="stylesheet" href="styles.css">

<button id="open-dialog">Open Dialog</button>

<div id="custom-dialog" role="dialog" aria-modal="true" aria-labelledby="dialog-title" class="dialog">
  <div class="dialog-content">
    <h3 id="dialog-title">Confirm Action</h3>
    <p>Are you sure you want to delete this file?</p>
    <div class="dialog-actions">
      <button id="confirm-btn">Yes</button>
      <button id="close-dialog">Cancel</button>
    </div>
  </div>
</div>

<script src="index.js"></script>
```

### Abstract role
- These roles help organize the document. They're only meant to be used internally by the browser, not by devs, so you should know that they exist but you shouldn't use them on your websites or web applications.


