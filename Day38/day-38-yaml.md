# Day 38 – YAML Basics

### Task 1: Key-Value Pairs
Create `person.yaml` that describes yourself with:
- `name`
- `role`
- `experience_years`
- `learning` (a boolean)

**Verify:** Run `cat person.yaml

<img width="491" height="115" alt="image" src="https://github.com/user-attachments/assets/f8aa48f1-49a5-4745-b2a3-efacc9884255" />

---

### Task 2: Lists
Add to `person.yaml`:
- `tools` — a list of 5 DevOps tools you know or are learning
- `hobbies` — a list using the inline format `[item1, item2]`

   <img width="498" height="247" alt="image" src="https://github.com/user-attachments/assets/b9de6986-5c2c-4786-ae45-57ada0250f5f" />

  Write in your notes: What are the two ways to write a list in YAML?
   1. `**Block-style**` ->
     -  Each line start with dash(-) followed by space
     -  this is the most common and readble format

    <img width="190" height="121" alt="image" src="https://github.com/user-attachments/assets/737fd5b7-0793-43a5-99f6-342af5c37041" />

  2. `**Inline format**`
     - Items are enclosed in [] and separated by commas(,)
     - Similar to JSON array syntax
       
   <img width="473" height="19" alt="image" src="https://github.com/user-attachments/assets/b6f2eeff-60cb-47c4-8673-7fcc0c7c53ec" />

---

### Task 3: Nested Objects
Create `server.yaml` that describes a server:
- `server` with nested keys: `name`, `ip`, `port`
- `database` with nested keys: `host`, `name`, `credentials` (nested further: `user`, `password`)

  <img width="488" height="288" alt="image" src="https://github.com/user-attachments/assets/c6dc546d-e32c-4c9b-abfa-3697ba7a0cf9" />


**Verify:** Try adding a tab instead of spaces — what happens when you validate it?

---

### Task 4: Multi-line Strings
In `server.yaml`, add a `startup_script` field using:
1. The `|` block style (preserves newlines)
2. The `>` fold style (folds into one line)

   <img width="865" height="545" alt="image" src="https://github.com/user-attachments/assets/04696bfe-5f86-4156-9c33-f148e840b7a4" />


Write in your notes: When would you use `|` vs `>`?
  # YAML Multi-line Strings: `|` vs `>`

- **`|` (Literal Block)**
  - Preserves **all line breaks** exactly as written.
  - Use for **scripts, config files, SQL queries, or any text where formatting matters**.

- **`>` (Folded Block)**
  - Folds lines into a **single line**, converting line breaks to spaces.
  - Use for **long descriptions, paragraphs, or text that should be one continuous line internally**.  

---

### Task 5: Validate Your YAML
1. Install `yamllint` or use an online validator
2. Validate both your YAML files

    <img width="813" height="399" alt="image" src="https://github.com/user-attachments/assets/8e5be188-14de-42fc-af0d-511c9fa962c5" />

    <img width="888" height="435" alt="image" src="https://github.com/user-attachments/assets/43e60a7c-06d3-448b-83db-093f283a7ddb" />


3. Intentionally break the indentation — what error do you get?

      <img width="908" height="449" alt="image" src="https://github.com/user-attachments/assets/d5d9edaa-dea3-42ea-8f4c-0d540599254a" />

      - **Error* -> Map keys must be unique at line 18, column 5



4. Fix it and validate again

    <img width="763" height="340" alt="image" src="https://github.com/user-attachments/assets/ff3324df-b1b1-4c90-b792-dd0e15d69961" />


---


