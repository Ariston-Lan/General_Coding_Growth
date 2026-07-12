# How Do you Display Mathematical Equations and Chemical Formulas in HTML?

## Superscript Element
- The superscript element is sued to display a piece of text as a superscript. A superscript is a symbol or letter printed above the normal line of text.

- For people who are dumb like, it just means the tiny number ABOVE whatever character you choose to input

### Example
```html
<p>2<sup>2</sup> = 4</p>
```

## Subscript element
- Does everything the sueprscript element does, just a subscript instead

### Example
```html
<p>H<sub>2</sub>O is the element of water!</p>
```

# How Do You Represent Computer Code in HTML?

## Inline Code Element
- The inline code element is used to represent short snippets of code inside text. Commun use cases for the code element would be for technical articles and document pages.

### Example
```html
<p>
    To set the text color to blue in CSS, use the following code:
    <code>color: blue;</code>
</p>
```

## Preformatted text element
- The code element is meant to only be used for a single line of code. If you want to include multiple lines of code, you'll have to use the <pre> element.

### Example
```html
<pre>
    <code>
        body {
            color: red;
        }'
    </code>
</pre>
```

# What Are the U, S, and Ruby Elements Used For, and How Do They Work?

## Unarticulated Annotation Element
- The unarticulated annotation element, or <u>, is used to represent inline text that has non-textual annotation applied

### Example
```html
<p>
    You can use the unarticulated annotation element to highlight
    <u>inccccort</u> <u>spling</u> <u>isses</u>.
</p>
```

## Strikethrough Element
- The strikethrough element, or <s>, is used to represent text that is no longer accurate or relevant. 

### Example
```html
<p><s>Tomorrow's hike will be meeting at noon</s></p>

<p>Due to unforseen weather conditions, the hike has been cancelled.</p>
```

## Ruby elemet
- The <ruby> element represents small text shown above or below the main text. It is typically used to show the pronounciation of East Asian characters.

### Example
```html
<ruby>明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp> </ruby>
```

- The rp element is used as a fallback for browsers lacking support for displaying ruby annotations.

- The rt element is used to indicate the text for the ruby annotation. This text is usually used for pronounciation.
