# Why Should You Care About Semantic HTML?

## Semantics
- Semantics are the meanig of words, or phrases in a language. In HTML, elements have their own semantic meanings too.

- The semantic meaning of an element refers to what special information that element conveys. The semantic meaning of a p element for example, is a paragraph of text.

- Most elements have semantic meaning, but some do not (such as div element).

# Why is it Important to Have Good Structural Hierarchy?

## Structural Hierarchy and Its Importance
- Your Structural Hierarchy refers to how you structure your page, such as the order on the usage of certain elements.

- This is important because of what these elements represent, for example your h1 element is your top level heading. You will rarely have more than one of these on a page, and it should typically come before all your other content. Your h2 element is your subheading, and should always come after your h1 element.

- You shouldn't use the different heading elements simply because of their larger text (that's what CSS is for), instead use them to create a page structure that is easy to read and follow.

# What is the Difference Between Presentational and Semantic HTML?

## Presentational HTML
- Presentational HTML focuses on the appearance and style of the content. 

- Presentational HTML is mainly outdated and not used as CSS and other means of getting the text to change exists.

- Some depracted presentational html elements are center, font, and big

### Example:
```html
<font size="5" color="red">This text is red and large.</font>
```

## Semantic HTML
- Search engines can easily understand your website when you use semantic HTML. It's also helpful for accessibility purposes, because screen readers need semantic information to describe what's on the web page.

### Example:
```html
<header>
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>
</header>
```

# When Should You Use the Emphasis Element Over the Idiomatic Text Element?

## Idiomatic Text Element
- The idiomatic text element, i, was originally used for presentational purposes to display the text in italics. But now, it is frequently used for highlighting alternative voice or mood.

### Idiomatic Example
```html
<p>There is a certain <i lang="fr">je ne sais quoi</i> in the air.</p>
```
- The lang attribute inside the open <i> tag is used to specify the language of the content. The i element does not indicate if the text is important or not, it only shows that it's somehow different from the surrounding text

- If you DO need to emphasize the importance of the text, you can use a similar semantic element, <em>

### <em> Example
```html
<p>
    Never give up on <em>your</em> dreams
</p>
```

# When Should You Use the Strong Element Over the Bring Attention To Element?

## Bring Attention element <b>
- The "bring attention to" element, <b>, is commonly used to highlight keywords in summaries or product names in reviews. Usually browsers display this text in boldface.

### <b> Example
```html
<p>
    We have tested a lot of strategies to win in brawlstars.
    There is the <b>bullshit strategy</b> which relies on total bullshit but its still kinda good and there is also the <b>only use meta brawlers strategy</b> which is boring but effective!
</p>
```
- If you need to emphasize the IMPORTANCE of the text, you should use the <strong> element instead of the <b> element

## Strong element
- Strong is a semantic HTML element that emphasizes the text is crucial, or urgent. 

### <strong> Example
```html
<p>
    <strong>WARNING:</strong> This product may kill you...sorry!
</p>
```

#### <strong> vs <b>
- <strong> signifies IMPORTANCE
- <b> is just to draw the users attention without indicating a higher level of importance

