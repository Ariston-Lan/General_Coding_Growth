# What Is the Difference Between Slashes, a Single Dot, and Double Dot in Path Syntax?

## File paths
- Look at these links:
/public/logo.png
./script.js
../style.css
- Notice how each of them have either a slash, a single dot, or a double dot? Each of these symbols hold significance in a file path

### The Slash
- The slash is the "path seperator". It's used to indicate a break in the text between folder or file names. 
    *  naomis-files/ --> points to a directory of that same name

    * naomis/files/ --> points to a files directory in the naomis directory

### The Single Dot and Double Dot
- A single dot points to the current directory while the double dot points to the parent directory.

#### Example:
my-app/
├─ public/
│  ├─ favicon.ico
│  ├─ index.html
├─ src/
│  ├─ index.css
│  ├─ index.js

- Given this file tree, if your public/index.html needed to load favicon.ico file, you would use a relative path with a single dot (since both files are in the same place)
    * ./favicon.ico

- If your public/index.html needed to load index.css file, you would use a relative path with double dots to naviagte tot he parent my-app directory first, then go to the src directory.
    * ../src/index.css

# What Are the Different Link States, and Why Are They Important?

## Link State
- When a link on a web page becomes purple after you click it, this occurs because the state of the link has changed, so different styling gets applied.

- There are 5 different states a link can be in.

### :link
- :link ; this state represents a link which the user has not visited, clicked, or interacted with yet.

### :visited
- :visited ; this state applies when a user has visited the page being linked to. By default, this turns the link purple, but you can leverage CSS to provide a different visual indication to the user.

### :hover
- :hover ; this state applies when a user is hovering their cursor over a link. This state is helpful for providing extra attention to a link, to ensure a user intends to click it.

### :focus
- :focus ; This state applies when we focus on a link (using tab to navigate links)

### :active
- :active ; This state applies to links that are being activated by the user. This typically means clicking on the link with the primary mouse button by left clicking.

## Specific Link State Order
- For CSS you should order your link states like this
 * link, visited, hover, focus, then active