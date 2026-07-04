# What Are Description lists, and When Should You Use Them?

## Description Lists
- Used for presenting terms and definitions in an orgsanized and easy-to-read format, like in a glossary or a real dictionary, where you can find words with their corresponding definitions.

### Example
```html
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
    <dt>CSS</dt>
    <dd>Cascading Style Sheets</dd>
</dl>
```

- The acronyms HTML and CSS are the terms, and the details are their expansions.

### Description List Elements
- dl: Container for the entire list
- dt: Description term
- dd: Description detail, used after each description term

# How Do Block and Inline Quotes Work in HTML?

## Quoted Elements - Block Quotes
- Quoted elements are used to distinguish quoted text from the surrounding content.
- Use the blockquote element for representing a section quoted from another source.

### Example
```html
<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    "Can you imagine what it would be like to be a successful developer? To have build software systems that people rely upon?"
</blockquote>
```
#### Cite Attribute
- The cite attribute is the URL of the source of the quote

## Quoted Elements - q element
- The q element is once again, for distinguishing quoted text from normal text but speciifically short quotes instead

### Example
```html
<p>
    As Martin Luther King once said,
    <q cite="https://www.martinlutherking.com">
        "If you can't walk crawl, but always keep moving."
    </q>
</p>
```

## Cite Element
- Used to mark up the title of a creative work

### Example
```html
<p>My favorite book is <cite>Diary of a Wimpy Kid</cite>.</p>
