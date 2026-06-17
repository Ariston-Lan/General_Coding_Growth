
# Day 28, HTML Fundamentals

# What are Div Elements and When Should You Use Them?

- <div>: Container to group other elements

## Example of <div>

```html
<div>
    <p> Example paragarph here </p>
    <p> Follow-up example paragraph </p>
</div>
```
--------

# What are IDs and Classes, and When Should You Use Them?

## IDs:

- id: adds a unique identifier to an HTML element
- You can reference the id name of title within Javascript or CSS

### Example of id:
```html
<h1 id='title'>Movie Review Page</h1>
<h2 id='subtitle'>Movie Review Subtitle</h2>
```

### Example of id being referenced (CSS):
```css
#title {
  color: red;
}
```
- Title id is being referenced which changes title heading to color red.

## Classes:

- classes: used to apply a set of styles to multiple elements
- You can reference classes within Javascript or CSS

### Example of classes:
```html
<div class="box"></div>
```
- You can also add multiple class names by seperating them within <div> via spaces.

```html
<div class="box red-box"></div>
```

### Example of classes being referenced (CSS):
```css
.box {
  width: 100px;
  height: 100px;
}

.red-box {
  background-color: red;
}

.blue-box {
  background-color: blue;
}
```
## Recap id vs classes:

- Classes are for applying a set of styles to MANY elements
- ids are for uniquely identifying specific elements

# What Are HTML Entities, and What Are Some Common Examples?

- HTML entity/character reference: Set of characters used to represent a reserved character in HTML
- They start with '&' and end with ';'
- These can be used to actually show characters such as <p> or special symbols such as the copyright symbol

## Example of named character reference:
```html
<p>This is an &lt;img/&gt; element</p>
&lt;p&gt;learning is fun&lt;/p&gt;
```
## Decimal numeric reference

- A type of character reference to get special characters specifically
- Starts with '&' followed by '#' and then one or more decimal digits, ends with ';'

## Example of Decimal numeric reference
```html
&#60;
&#169;
&#174;
```
- Some examples of the references being used to access special symbols

## HexaDecimal numeric reference

- Starts with '&' followed by '#' then 'x', contains one or more ASCII hex digits, ends with ';'

## HexaDecimal example:
```html
&#x3C;
&#x20AC;
&#x3A9;
```
- Some examples of the references being used to access special symbols

# What is the Role of the Script Element in HTML, and How Can it Be Used to Link to External JavaScript Files?

- <script> is used to embody executable code. Usually used for JavaScript code.
- JavaScript adds interactivity to webpages

## Example of script
```html
<body>
  <script>
    //alert('Welcome to twitter!');
  </script>
</body>
```
### Script Usage Disclaimer

- While you can technically write all of your JavaScript inside of the script element, its better to provide a link to an external JavaScript file is stead

#### Script Linkage Example
```html
<script> src="path-to-javascript-file.js"></script>
```
