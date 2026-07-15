# What Are Replaced Elements, and What Are Some Examples?

## Replaced Element
- A replaced element is an element whose content is determined by an external source rather than by CSS itself. 

- Common examples of replaced elements include image, iframe, and video elements.

- With replaced elements, you can control the position, or layout of an element. But your CSS cannot directly modify the content of that element.

### Example
```html
<img src="example-img-url" alt="Descriptive text goes here">
```
- The element itself is replaced with the external object: the image. Your CSS can control things like positioning or apply a filter to the image, but cannot actually modify the image itself.

- Another example of this is the iframe element, which embeds an external site on your web page.

### iframe elemnt
```html
<iframe width="400" height="200" src="https://www.youtube.com/embed/u43gJJrVa1I?si=BoDW_puFsy8OEr_Z" title="Professional Cloud Architect Certification Course – Pass the Exam! (YouTube video)" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

# How Do You Embed Videos onto Your Page Using the iframe Element?

## iframe attributes
- src: Where the external link goes
- width/height: determines each characteristic respectively
- allowfullscreen: Allows user to display iframe in full screen mode
- title: Specifies title of element for accessibility
- allow: Defines what the iframe can or can't do. The allow attribute is followed with an allowlist.

### Example:
```html
<h1>A Map from Openstreetmap.org Embedded with the iframe Element</h1>

<iframe
width="425"
height="350"
src="https://www.openstreetmap.org/export/embed.html?bbox=3.006134033203125%2C6.150112578753815%2C3.6357879638671875%2C6.749850810550778&amp;layer=mapnik"
title="Map of Lagos area, Nigeria"
style="border: 1px solid black"
>
</iframe>
<br />
<small>
    <a href=""https://www.openstreetmap.org/#map=11/6.4501/3.3210">
    View Larger Map
    </a>
</small>
```

# What Are the Different Target Attribute Types, and How Do They Work?

## Target attribute
- Target tells the browser where to open the URL for the anchor element

### Example:
```html
<a href="https://freecodecamp.org" target="_blank">Visit freeCodeCamp</a>
```

### Different Target Attribute Values
- _self: Opens the link in the current browsing context (current tab/window)
- _blank: Opens the link in a new browsing context (new tab or window)
- _parent: opens the link in the parent of current context (so if your website has an iframe, _parent would open in your website's tab/window, not in the embedded frame)
- _top: opens the link in the top most browsing context.
- _unfencedTop: Currently used for experimental FencedFrameAPI

# What Is the Difference Between Absolute and Relative Paths?
## Path
- A path is a string that specifies the loaction of a file or directory in a file system. (Like when you download a file and it asks for the path to the location where you want it to be stored)

- Paths let devs link to resourcs like images, stylesheets, scripts, and other web pages.

### Absolute Paths
- Absolute paths" A complete link to a resource. Starts from the root directory, includes every other directory, and finally the filename and extention. (The "root directory" referts to the top-level directory or folder in a hierarchy)

#### Example:
```html
<p>
    Read more on the
    <a
    href="/Users/user/Desktop/fCC/script-code/absolute-vs-relative-paths/pages/about.html">
    About Page
    </a
    >
</p>
```
- In this example we are starting from the root and going into a folder called users, then a folder called user, then a folder called Desktop, then fCC...and so on, until you finally get the about.html file.

### Absolute URL

- Absolute URL: A complete address used to access a resource. It includes the protocl (http, https, file, etc.) and the domain name. 

#### Example

```html
<a
href="https://design-style-guide.freecodecamp.org/img/fcc_secondary_small.svg">
View fCC Logo
</a>
```

### Relative Paths

- Relative paths: Specifies the location of a file relative to the directory of the current file. It does NOT include the protocol or the domain name, making it shorter and more flexible for internal links within the same website.

#### Example
```html
<p>
    Read more on the
    <a href="about.html">
        About page
    </a>
</p>
```

- In this scenario, imagine you are on a contact.html page, which is in the same folder as the about.html page. Since they are moth in the same place, you can simply use a relative path rather than an absolute one.



