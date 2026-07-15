# What Are the Roles of the aria-label and aria-labelledby Attributes?

## aria-label and aria-labelledby
- aria-label and aria-labelledby attributes provide crucial information about page elements that might be unclear or invisible

### aria-label
- aria-label is useful for elements that do not have visible text but still need to be described by screen readers

- For input elements, the aria-label attribute provides a label directly if there isn't a visible label associated with the input.

#### Example
```html
<button aria-label="Search">
    <i class="fa-solid fa-magnifying-glass"></i>
</button>
```


### aria-labelledby
- aria-labelledby attribute doesn the exact same thing as the aria-label attribute, but instead of defining the text directly in an attribute, you use a reference to text that already exists on the page. The existing text must have an id attribute, which will be useful for the reference value in the aria-labelledby attribute.

#### Example
```html
<input type='text' aria-labelledby="search-btn">
<button type="button" id ="search-btn">Search</button>
```

- In this case, the text for the button is being used as the label for the search input. Screenr eaders willa nnounce the input ass omething like "Search, edit". If you later decide you want to change the buttont ext to find, the label for the input will automatically be updated to the new text since it is referencing the button text.

- Combining multiple id values inot a single aria-labelledby attribute is also possible.

```html
<div>
    <span id='volume-label'>Volume</span>
    <span id="volume-details">Adjust the volume level</span>
    <input
    type="range"
    min="0"
    max="100"
    value="30"
    aria-labelledby="volume-label volume-details">
</div>
```

- For the slider, the screen reader will look out for the content of the volume-label and volume-details elements and announce Volume adjust the volume level.

# What Is the aria-hidden Attribute, and How Does It Work?

## aria-hidden
- If you ever need to display content while at the same time hiding it from people who use assistive technology, like screen readers, you can use the aria-hidden attribute.

- You just need to add it to the HTML element that you want to hide and set its value to true.

### Example
```html
<head>
  <!-- Font Awesome CDN -->
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.0/css/all.min.css"
  />
</head>

<button>
  <i class="fa-solid fa-gear" aria-hidden="true"></i>
  <span class="label">Settings</span>
</button>
```

- You do not need to use aria-hidden when: The HTML element already has a hidden status, the element or the element's ancestor is already hidden with display:none, or the element or the element's ancestor is already hidden with visibility:hidden

- Note that setting aria-hidden to ffalse will not expose the element to assistive technologies if any of it sparents has this attribute set to true.

# What Is the aria-describedby Attribute, and How Does It Work?

## aria-describedby
- The aria-describedby attribute is used to provide additional information about an element to screen reader users by referencing existing content on the page. It creates a progmattic association between the element and the content, which screen readers can use to inform users of the additional information when they interact with the element.

### Example
```html
<link rel="stylesheet" href="style.css">

<form>
  <label for ='password'>Password:</label>
  <input type="password" id="password" aria-describedby="password-help">
  <p id="password-help">Your password must be at least 8 characters long</p>
</form>

<script src="index.js"></script>
```
- We are using the aria-describedby attribute to associate the password input field with the password reequirements in the paragraph element. When a screen reader user interacts with this input, their screen reader will announce the name of the input (passwrod) and may then also announce the passwrod requirements.

- Another good case for teh aria-describedby attribute is when you have a delete button

```html
<button aria-describedby="delete-message">Delete</button>

<p id="delete-message">Warning! All deletions are permanent.</p>
```

# When Is the alt Attribute Needed, and What Are Some Examples of Good Alt Text?

## alt attribute
- Altnerative text is a brief text description of an image. It provides eessential information about the image for users who cannot see it, such as people who use screen readers or other assistive technologies.

- Good alt text is descriptive and conveys the meaning of the photo. Remember, you are describing an image to someone who litearlly, cannot see it.

- If your image is a link, like a right arrow that moves you to the next page for example, then describe where the link will take them rather than just saying "right arrow".

## null attribute

- Only images that convey important information should have lt text. If an image is only used for decorative purposes, it should have null (empty) alt text, so it can be ignored by screen readers and other assistive technologies.

### Example
```html
<img src="decorative_image.jpg" alt="" >
```

- EVERY image should have an alt attribute, even if it is empty. If you omit the alt attribute, screen readers will read the file name instead. 

# What Are the Accessibility Benefits for Good Link Text, and What Are Examples of Good Link Text?

## good link texts
- The first visible benefit of a good link text is that it makes it easier for everyone to find information quickly. Descriptive links help users know where they're heading and what they'll accesss. This ensures the user dosen't feel lost and improves the ovrerall user experience. 

- Making link text descriptive isn't just beneficial for those living with visual impairments. Descriptive links also help people with cognitive disablities by providing clear context.

### Example
```html
<a href="webinar-details-link">Details</a>
```
- Details is vague and does not provide speciifc infomration, therefore this is NOT a good link description

```html
<a href='webinar-details-link'>
  Get details about our upcoming webinar
  </a>
```
- This link text gives users context about the content they will find, making it easier to decide whether they want to click on it.



# What Are Good Ways to Make Audio and Video Content Accessible?

## track element
- The first thing you should consider doing is adding captions or subtitles to your video-content

- Captions provide the text version of spoken words and important non-verbal sounds, like music or laughter.

- Subtitles, on the other hand, are essential for people who don't understand the language you're speaking.

- To add captions or subtitltes to your video or audio content, you can use the track element inside your video or audio element.

### Example
```html
<video
  width="400"
  height="300"
  controls
  src="https://cdn.freecodecamp.org/curriculum/labs/what-is-the-map-method-and-how-does-it-work.mp4"
>
  <track
    src="captions.vtt"
    kind="captions"
    srclang="en"
    label="English"
  />
</video>

<audio controls src="sample.mp3">
  <track
    src="captions.vtt"
    kind="captions"
    srclang="en"
    label="English"
  />
</audio>
```

## kind, src lang, and label attribute
- The kind attribute is used to tell the element how it should be used. Valid values for kind include captions, subtitles, chapters, and metadata.

- srclang attribute represents the language for the track content.

- The label attribute is a descriptive title for the text track that broswers use to identify and display it in the list of avaliable text tracks.

# What Are Some Ways to Make Web Applications Keyboard Accessible?

## Tab
- Many users rely on the Tab key to move through interactive elements on a webpage. By default, browsers let users tab through elements like links, buttons, and form fieldss in the order they appear in the HTML. This is called the natural tab order.


# tabindex attribiute
- Sometimes you may want to adjust which elements are focusable or change their focus order. The tabindex attribute allows you to do this

### Example
<element tabindex="number">Element Text</element>

### tab index values

- The value of tabindex determines how the element behaves in keyboard navigation

- tabindex='0' adds the element to the natural taborder.

- tabindex='1' makes an element focusable programmatically, which is useful for managing focus in elements that are not normally focusable, such as headings, containers, dialogs, or error messages.

- When a tab index is greater than 0, it sets a custom tab order. So elements with lower positive values are focused first

## accesskey attribute
- accesskey allows you to define a key that focuses on or activates a particular element.

### Example
```html
<button accesskey="s">Save</button>
<button accesskey="c">Cancel</button>
<a href="index.html" accesskey="h">Home</a>
```
