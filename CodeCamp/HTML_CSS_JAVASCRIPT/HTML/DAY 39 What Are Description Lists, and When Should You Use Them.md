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
```

# How Do You Display Abbreviations in Html?

## Abbreviations
- Abbreviation is a shortened form of a word. Like Dr. = doctor
- There are two common forms of abbreviations: acronyms and initialisms.

### Acronyms
- An acronym is a word formed from the initial letters of a phrase, with each letter representing the first letter of a word in that phrase. An example of this is GUI, which stands for Graphical User Interface. By thaking the first letters you get the acronym GUI.

### Initialisms
- An initilalism is formed from the initial letters of  a phrase, with each letter representing the first letter of a word in that phrase. An example of this is HTML, which stands for HyperText Markup Language, and is pronounced by spelling out each letter, HTML.

### Abbreviation Element
- <abbr>HTML</abbr> --> This is an example of the abbreviation element. To properly use it, you surround the abbreviated phrase in the element. This can be done within a paragraph or heading alike.

#### Example
```html
<p><abbr>HTML</abbr> is the foundation of the web!</p>
```

### Title element
- If you want to help users understand what the acronym means, you can use the title attribute

#### Example
```html
<p><abbr title="HyperText Markup Language">HTML</abbr> is the foundation of the web!</p>
```

# How Do You Display Addresses in HTML?

## Contact Address Element
- The contact address element is used to represent contact information for a section on a web page.

- The <address> element is versatile and can be used for buisness pages, author pages, personal sites, and more.

### Example
```html
<address>
    <h2>Company Name</h2>
    <p>
        1234 Elm Street<br />
        Springfield, IL 62701<br />
        United States
    </p>
    <p>Phone: <a href="tel:+15555555555">+1 (555) 555-5555</a></p>
    <p>Email: <a href="malito:contact@company.com">contact@company.com</a></p>
</address>
```
- The br element is used for line breaking
- Both the tel:+ attribute and the mailto attribute are used for telephone numbers and emails respectively. However the malito link is often percieved as spam, so keep that in mind when using it!

# How Do You Display Times and Dates in HTML?

## Time element
- the <time> element is used to represent a specific moment in time

### Example
```html
<p>The reservations are for <time datetime="20:00"></time>
```

#### datetime attribute
- The datetime attribute is used to translate dates and times into a machine readable format. This is important because it helps with search engine results and helps the browser process date and time information more effectively.

- The value for the datetime attribute must be a valid year, valid month,valid time, local date, global date, or valid duration string.

##### Example 
```html
<p>
    The graduation will be on <time datetime="2024-06-15T15:00">June 15
</p>
```
- The value for datetime attribute here is in the ISO 8601 format. ISO 8601 is an international standard to represent dates and times. The first part of that value is the year, month, and day, and the capital T is the separator between the date and time.