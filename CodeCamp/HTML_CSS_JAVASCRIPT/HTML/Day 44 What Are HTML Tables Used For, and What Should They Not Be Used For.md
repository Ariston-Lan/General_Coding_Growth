# What Are HTML Tables Used For, and What Should They Not Be Used For?

## HTML tables
- HTML tables aren't used much these days as they used to be, so fair warning. Tables are one of the eraliest ways devs had for displaying data in a browser way back in the 1990s.

## table elements/table hierarchy
- Tables are structured almost like minature wepbages. They include mutliple elements.

- <table> This is the element in which the entire table is contained

- <thead> This is the table's head

- <tr> This is where the data itself is always contained

- <th> This is where the text would go. Since this is data it would first go in the <tr> element

- <tbody> This is the table's body, similar to a websites <body>

- <td> This is data cells that appear on the side of your table

### Example
```html
<table>
    <thead>
        <tr>
            <th>The title of this table</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>First Row</th>
            <td>First Data Cell</td>
        </tr>
        <tr>
            <th>Second Row</th>
            <td>Second Data Cell</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th>The footer of thsi table, which might contain date of publication, author credits, or meta information</th>
        </tr>
    </tfoot>
</table>
```

# What Is an HTML Validator, and How Can It Help You Debug Your Code?

## HTML Validator
- Essentially it is a tool that parses your code and checks for any structural inconsistencies that do not match the standard HTML structure.

- When you visit the site validator.w3.org, you can click on the Validate by Direct Input button and paste in your HTML code.

- Another HTML validator that you can use is jsonformatter.org

# How to Use the DOM Inspector and DevTools to Debug and Build Your Projects

## DOM
- The DOM stands for Document Object Model. it is a tree-like structure that represents the elements on a page.

## DevTools
- The developer tools allow you to inspect the HTML, CSS and JavaScript of the page you are on (Ctrl + Shift + i)

- When you open the developers tools in google chrome you'll see a number of tabs. 

- Elements tab; this shows you the html structure of the page you are on

- Cosnole tab; this shows you any errors that might be occurring on the page

# What Is Accessibility?

## Accessibility
- Accessibility involves creating products and services that everyone can use. in the context of web development, its making websites that everyone can understand and interact with, including people with visual, auditory, motor and cognitive disabilites.

### W3C
- To help you create accessible websites, the World Wide Web Consortium, known as W3C, deceloped a set of international standards that you can follow to make your websites more accessible and easier to use for people with disabilities.

These standards are known as the Web Content Accessibility Guidlines (WCAG)

### POUR
- These guidelines are designed with four core principles in mind, known as POUR

- P stands for Perceivable. Users must be able to percieve the information you ar epresenting. For example, you can provide an alternative text for images, so users who access your website with a screen reader can understand them.

- O stands for Operable. Users must beable to interact with the user interface. For example, you can make sure that all functionality is accessiblte through the keyboard too, not just the mouse.

- U stands for understandable. Users must be able to understand the information. For example, you can avoid complex sentences and use simple language as much as possible

- R stands for Robust. A wide range of browsers and other tools, including assistive technologies, must be able to interpret the content

# What Are Screen Readers, and Who Uses Them?

## Screen readers
- Screen readers are assistive technology programs that help blind and visually impaired people use computers and mobile devices

- Always make sure your website is accessible to these devices

# What Are Large Text or Braille Keyboards, and Who Uses Them?

## Large Text/Braille Kayboards
- Large text and braille kayboards are designed for users with visual disbailities. In Large Text Keyboards, also called Large Print Kayboards, the letters, numbers, and symbols, are larger compared to standard keyboards. This design is helpful for people who may find smaller text in the keys difficult to see. Most of them also have enhanced contrast and brightness.

# What Are Alternative Pointing Devices Such as Trackballs, Joysticks, and Touchpads Used For?

## Alternative Pointing Devices
- Alternative poitning devices are input devices that make good alternatives to the traditional mouse. They are essential for improving computer accessibility for those with disabiilities, forelimb impairments, and limited mobility.


# What Are Screen Magnifiers Used For?

## Screen Magnifiers
- Screen magnifiers are tools that help people with low vision and other visual impairments better access digital content and the web.

# What Is Voice Recognition Software Used For?

## Voice Recognition Software
- Voice recognition helps people with disabilities interact with computers and other digital devices. Voice recognition tools let people with disabilities use their voice to pass commands to perform various tasks instead of using traditional inputer devices like keyboards and mice. Because voice recognition software tools elimainate the need for physical interaction, they empower people with disabilities with significant independence and control over their environment

# What Are Some Common Accessibility Auditing Tools to Use?

## Accessibility Auditing Tool
- Ana ccessibility auditing tool is an application that helps you improve the accessibility of your digital content by reporting accessibility issues that can be easily found through automated testing. This content includes websites, web applications, and mobile apps.

### Free accessibility tools
- Google Lighthouse: You can check SEO, accessibility, best practices, and perfomance

- WAVE: Chrome extention or web. 

- IBM Equal Access Accessibility Checker: Scan websites for accessibility issues and generate a detailed report

# How Does Proper Heading Level Structure Affect Accessibility?
- Proper us eof headings creates a visual hierarchy for users to navigate and understand your web page. Using a logical heading hierarchy allows screen reader users to understand the structure of your content and navigate your content quickly. Creating appropriate heading text that accurately describes the content that follows helps everyone find the information they need on your site. They also may improve the SEO of your page.

# What Are Best Practices for Tables and Accessibility

## Accessible tables

### Caption Element
- The first best practice we will cover is using a table caption. With the <caption> element, you can write the caption (or title) of a table, so users, especially those who use assistive technologies, can quickly understand the table's purpose and content. You should place the caption element immedieately after the opening tag of the table element. This way, screen readers and other assistive technologies cna provide more context by announcing the caption BEFORE reading the content.

### Table Headers (<th>)
- You can define a row or column header with the table header element, <th>. Associating the data cells with their corresponding headers is also very important for screen  readers. 

### Scope Attribute
- The <scope> attribute determines if a header is a row header or a column header. Screen readers may guess this correctly from the table's structure, but it's usually reccomended to explicitly indicate the scope to ensure calrity.

- The scope attribute has four possible values. col, for collumn, and row, for row.

#### Example
```html
<table>
    <caption>Our Pets</caption>
    <thead>
        <tr>
            <th scope='col'>Name</th>
            <th scope='col'>Age</th>
            <th scope='col'>Type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope='row'>Nora</th>
            <td>5</td>
            <td>Dog</td>
        </tr>
        <tr>
            <th scope='row'>Gino</th>
            <td>2</td>
            <td>Cat</td>
        </tr>
    </tbody>
</table>
```

- If a column or row header spans across multiple cells, the scope will also be applied to each one of the cells individually.

# Why Is It Important for Inputs to Have an Associated Label?

## Labels
- Screen readers rely on labels to describe the purpose of input fields. In order for this to work properly, the label must be programmatically associated with the input. While there are several ways to do that the, the most common is to use the HTML label element.

### Example
```html
<form>
    <label for="name">Your Name
        <input type="text" id="name">
    </label>
</form>
