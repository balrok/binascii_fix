# bin ascii fixer

In cases where a binary file is transfered in ascii format via FTP.
This fixer will brute force all possible original files.


## What happens when transfering a binary file in ASCII mode

Since this kind of transfer will replace any of the following

```
\n -> \r\n (unix to windows)
\r -> \n (windows to unix #1)
\r\n -> \n (windows to unix #2)
```

we can not know 100% what the original file looked like.

## Examples (where people had the same problem)

* https://superuser.com/questions/195612/recovering-corrupted-files-uploaded-in-wrong-ftp-mode
    * first answer is actually how I implemented this
* http://blog.deepcore.gr/?p=177
    * "fixgz" did not work for me
* https://www.inmotionhosting.com/support/website/file-management/corrupt-file-ftp-transfer
    * how to avoid (but still happened to me in filezilla with auto)

## How to Use

`./fix.py folder`

## Example Data

Inside `demo_data` are two images. Just run `./fix.py demo_data` and then do `ls demo_data`.
