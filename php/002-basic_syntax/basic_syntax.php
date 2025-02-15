<?php
    # When PHP parses a file, it looks for its opening and closing tags.
    # Which tell PHP to start and stop interpreting the code between them.
    # Everything outside of the pair of opening and closing tas is ignored by 
    # PHP parser.

    # When the PHP interpreter hits the closing tag, it simply starts 
    # outputing whateber it finds (except for the immediately following 
    # newline) until it hits another opening tag.

    # If in the middle of a conditional statement, the interpreter will 
    # determine the outcome of the conditional before making a decision of 
    # what to skip over.

    # For outputing large blocks of text, dropping out of PHP parsing mode 
    # is generally more efficient than sending all of the text through echo
    # or print.

    # PHP supports 'C', 'C++' and Unix shell-style comments:
    # //, /* */ and #
?>

<?php
    if (str_contains($_SERVER['HTTP_USER_AGENT'], 'Firefox')) {
?>
<h3>str_contains() returned true</h3>
<p>You are using Firefox</p>
<?php
    } else {
?>
<h3>str_contains() returned false</h3>
<p>You are not using Firefox</p>
<?php
    }
?>

<?php echo 'this is the long form of printing a string' ?>
<?= 'this is the short form' ?>

<?php
    # Note that short tags can be disabled so to maximise compatibility you
    # should only use normal tags

    # If a file contains only PHP code, it is preferable to omit the PHP 
    # closing tag at the end of the file. This prevents whitespace or new 
    # lines being added after the PHP closing tag.
?>

The closing tag for the block will include the immediately trailing newline
if one is present.

<?php echo "Some text"; ?>
No newline
<?php echo "But newline now"; ?>

Outputs:
Some textNo newline
But newline now
