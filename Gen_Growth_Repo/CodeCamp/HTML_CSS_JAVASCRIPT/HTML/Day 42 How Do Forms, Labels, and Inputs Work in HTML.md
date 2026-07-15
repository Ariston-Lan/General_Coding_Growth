# How Do Forms, Labels, and Inputs Work in HTML?

## form Element
- The <form> element in HTML is used to gather user information, such as names and email addresses.

### Action attribute
- The action attribute specifies where the form data will be sent upon submission.

#### Example
```html
<form action="url-goes-here">
    <!-- input elements go here-->
</form>
```

## input Element
- To collect specific information, like names and email addresses, you would use the <input> element.

- input elements are void elements and do not have closing tags

### Example
```html
<form action="">
    <input type="text">
</form>
```

## label Element
- By nesting the label and input element within the form element, you can implicitly create an association between the two. Essentially saying that this input is for this purpose

### Example
```html
<form action="">
    <label for="email">Email Address: </label>
    <input type="email" id="email">
</form>
```

## placeholder attribute
- The placeholder attribute is used to give additional hints as to how the form is supposed to be correctly filled out

### Example
```html
<form action="">
    <label for="email">Email Adress: </label>
    <input type="email" id="email" placeholder="example@email.com">
```
# What Are the Different Types of Buttons, and When Should You Use Them?

## button Element
- The button element is used to perform a particular action when it is activated.

### Example
```html
<button>Start Game</button>
```
## type Attribute
- The button element has a type attribute which controls the behavior of the button when it is activated. The first possible value would be the button type.

- Another possible value for the type attribute is the submit value.

- The third possible value for the type attribute is the reset value

### Example
```html
<button type="button">Show Alert</button>

```html
<form>
    <label for="email">Email Address: </label>
    <input type="email" id="email" name="email">
    <button type="submit">Submit Form</button>
</form>
```
- In this example, when the submit button is pressed their data will be sent to the server and will be processed.

```html
<form action="">
    <label for="email">Email Address: </label>
    <input type="email" id="email" name="email">
    <button type="reset">Reset Form</button>
    <button type="submit">Submit Form</button>
</form>
```
- The reset button will clear out all of their input data. These buttons aren't usually the best idea because it literally wipes all user data, so use with caution.

## input Element
- Anoher way to create buttons in HTML is to use the input element. The input element also has a type attribute with possible values of submite, reset, and button. 

### Example
```html
<input class="start-btn" type="button" value="Start Game">
```

# What Is Client-Side Form Validation in HTML Forms, and What Are Some Examples?

## Brief Summary

- When a user filles out a form on your website, it is important they fill out ALL of the necessary information in the correct format. HTML form controls, like inputs, have a lot of built in validation that you can use to check for invalid data. This well help ensure that the user fixes these mistakes before the information is submitted and processed by the server.

- The term "client-side" referes to everything that happens on the user's computer or device, like the part of a website or app you interact with directly. This includes layout, design, and any interactive features.

- While client-side validation is important, you also need server-side validation for added security. Malicious users can bypass client-side checks, so robust server-side measures are essential.

## required Attribute
- The required attribute specifies that the user needs to fill out that portion of the form before it gets submitted. 

### Example
```html
<form action="">
    <label for="email">Email Address: </label>
    <input required type="email" name="email" id="email">
    <button type="submit">Submit Form</button>
</form>
```

## min and maxlength attributes
- These are additional validation attributes you can add within your input element 
to increase validation

### Example
```html
<form action="">
    <label for="email">Email Address: </label>
    <input required
    type="email" 
    name="email" 
    id="email"
    minlength="4"
    maxlength="64"
    />
    <button type="Submit">Submit Form</button>
</form>
```

# What Are the Different Form States, and Why Are They Important?

## Form States Definition
- Form controls, like inputs, can be in different stages or conditions like a focused state, a readonly state, or disabled state. Form control elements are elements that are nested inside the form element, and allow users to input, select, or submit data.

### Form States
- The first state is the default state. The default state of an email address input is a blank input.

- The second state is the focused state. When a user clicks on a form control or selects it with the keyboard's tab key, then that means it is in the focused state.

- The third state is the disabled state. This state shows user that an input cannot be focused or activated.

- Another type of state is the readonly state. This is when a form control, like an input, is not editable by the user.