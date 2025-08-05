## `encode`
Convert **binary data** into a textual representation, using a specified encoding format such as:
- `base64`
- `hex`
- `escape`
```PostgreSQL
-- Signature
-- encode(data bytea, format text) -> text

SELECT encode('hello'::bytea, 'hex'); -- 68656c6c6f, hex representation of 'hello' bytea.
```
## `decode`
Used to convert encoded text (like `base64` or `hex`) back into binary (`bytea`) format.
```PostgreSQL
-- Signature
-- decode(string text, format text) -> bytea

-- Decoding FROM hex
SELECT decode('68656c6c6f', 'hex')::text;
-- hello, hex representation got converted to binary and from binary to text again with final type conversion ::text
```
## `convert_from`
Used to convert binary data into a text string using a specified **character encoding**:
- `UTF8`
- `LATIN1`
- `SQL_ASCII`

Use this when you know the binary data represents a string encoded in a specific character set, and you want to convert it to **readable text**.

```PostgreSQL
-- Signature
-- convert_from(bytea_string, encoding_name)

-- Converting the hex representation of "Hello, World!" in UTF-8.
SELECT convert_from(E'\\x48656c6c6f2c20576f726c6421'::bytea, 'UTF8');
```
## `convert_to`
Converts text into a binary data using a specified character encoding:
- `UTF8`
- `LATIN1`
- `SQL_ASCII`

```PostgreSQL
-- Signature
-- convert_to(bytea_string, encoding_name)

-- Converting the string "Hello, World!" using the UTF-8 encoding.
SELECT convert_to('Hello, World!', 'UTF8');
```