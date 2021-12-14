# WalkSFTP

This is project is a class that allows for a glob like sftp download to a temporary file and lets you process the downloaded data using processing_function. The log argument can be used to check if the get and process ran correctly so you can run and not pull files that have already been processed and keeps track of files based on their modified time. This uses threading to separate the glob sftp files and the process function.

## Installation

Run the following to install:

```python
pip install walk_sftp
```

## Usage

```
from walk_sftp import WalkSFTP

def process(f)

	try:
		# if successfull
		return True
	except:
		# if unsuccessfull
		return False

WalkSFTP(
    ftp_web_address,
    username,
    password,
    start_date='2020-12-25', # optional
	end_date='2020-12-28', # optional
    print_out=True, # optional
    processing_function=process, # optional
    log='/some_path_to_log.p', # optional
)


WALK SFTP
'''
	Parameters
	----------
	base_url : str
			URL that you are pulling the SFTP
	username : str
			Username to login to the SFTP
	password : str
			Username to login to the SFTP
	port : int
			port
	store : None, str
			Path after to store files. If None, then
			stores in a temporary directory. Use with
			1) processing_function argument to get
			data from them and a log filepath to keep
			track of files already downloaded
	processing_function : None/function
			pass function if you want to process the
			data after sftp pull. Takes teh filepath as an
			argument. Returns True/False depending on whether
			the process ran correctly
	log : str
			filepath of log to get information on data.
			This can be used for a temporary directory
			in order to not keep the files stored but
			know that the data is processed. Should be
			a .p file
	blocks : list
			list of str to block. Looks for string
			in file path of each entry in blocks
			to determine whether to pull
	start_date : str/datetime
			date to only pull files that were modified after
			this date - default 1970-01-01

	Optional Args
	-------------
	print_out : bool
			Whether to print out messages (slower when True)
	break_count : int
			stop running sftp download after n number of files downloaded
	force : bool
			force to overwrite log that is in progress
	sleep_count : int
			number of seconds to wait until process and store threads
			time out. Default None
	must_have : str/list
			must include text in FTP download


```

## Development walk_sftp

To install walk_sftp, along with the tools you need to develop and run tests, run the following in your virtualend:
```bash
$ pip install -e .[dev]
```
