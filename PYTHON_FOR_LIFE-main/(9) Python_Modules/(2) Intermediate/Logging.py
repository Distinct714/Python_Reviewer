# LOGGING MODULE


# Logging is a means of tracking events that happen when some software runs. 
# It is also used to log information when testing or running software.
# The software’s developer adds logging calls to their code to indicate that certain events have occurred. 
# An event is described by a descriptive message which can optionally contain variable data
# Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

import logging
# The default level is WARNING, which means that only events of this severity and higher will be tracked, 
# unless the logging package is configured to do otherwise.

# If you want to change it, we can do that by setting the basic configuration (basicConfig) and specify some arguments:
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%y %H:%M:%S')


# FIVE DIFFERENT LOG LEVELS

# DEBUG is used for detailed information, typically of interest only when diagnosing problems.
logging.debug("This is a debug message.")

# INFO is used for confirmation that things are working as expected.
logging.info("This is an info message.")

# WARNING is used for indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). 
# The software is still working as expected.
logging.warning("This is a warning message.")

# ERROR is used when the software has not been able to perform some function due to a more serious problem.
logging.error("This is an error message.")

# CRITICAL is used when there is a serious error, indicating that the program itself may be unable to continue running.
logging.critical("This is a critical message.")


# DIFFERENT KEYWORD ARGUMENTS IN BASIC CONFIGURATION

# filename = It specifies that a FileHandler be created, using the specified filename, rather than a StreamHandler.

# filemode - If filename is specified, open the file in this mode. Defaults to 'a'.

# format - Use the specified format string for the handler. Defaults to attributes levelname, name and message separated by colons.

# datefmt - Use the specified date/time format, as accepted by time.strftime().

# style - f format is specified, use this style for the format string. One of '%', '{' or '$' for printf-style, str.format() or string.Template respectively. Defaults to '%'.

# level - Set the root logger level to the specified level.

# stream - Use the specified stream to initialize the StreamHandler. Note that this argument is incompatible with filename - if both are present, a ValueError is raised.

# handlers - If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don’t already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with filename or stream - if both are present, a ValueError is raised.

# force - If this keyword argument is specified as true, any existing handlers attached to the root logger are removed and closed, before carrying out the configuration as specified by the other arguments.

# encoding - If this keyword argument is specified along with filename, its value is used when the FileHandler is created, and thus used when opening the output file.

# errors - If this keyword argument is specified along with filename, its value is used when the FileHandler is created, and thus used when opening the output file. If not specified, the value ‘backslashreplace’ is used. Note that if None is specified, it will be passed as such to open(), which means that it will be treated the same as passing ‘errors’.