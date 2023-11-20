# Copyright 2010-2024 The pygit2 contributors
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2,
# as published by the Free Software Foundation.
#
# In addition to the permissions in the GNU General Public License,
# the authors give you unlimited permission to link the compiled
# version of this file into combinations with other programs,
# and to distribute those combinations without any restriction
# coming from the use of this file.  (The General Public License
# restrictions do apply in other respects; for example, they cover
# modification of the file, and distribution when not linked into
# a combined executable.)
#
# This file is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301, USA.

from enum import IntEnum, IntFlag

from . import _pygit2
from .ffi import C


class ApplyLocation(IntEnum):
    """ Possible application locations for patches """

    WORKDIR = _pygit2.GIT_APPLY_LOCATION_WORKDIR
    """
    Apply the patch to the workdir, leaving the index untouched.
    This is the equivalent of `git apply` with no location argument.
    """

    INDEX = _pygit2.GIT_APPLY_LOCATION_INDEX
    """
    Apply the patch to the index, leaving the working directory
    untouched.  This is the equivalent of `git apply --cached`.
    """

    BOTH = _pygit2.GIT_APPLY_LOCATION_BOTH
    """
    Apply the patch to both the working directory and the index.
    This is the equivalent of `git apply --index`.
    """


class AttrCheck(IntFlag):
    FILE_THEN_INDEX = C.GIT_ATTR_CHECK_FILE_THEN_INDEX
    INDEX_THEN_FILE = C.GIT_ATTR_CHECK_INDEX_THEN_FILE
    INDEX_ONLY = C.GIT_ATTR_CHECK_INDEX_ONLY
    NO_SYSTEM = C.GIT_ATTR_CHECK_NO_SYSTEM
    INCLUDE_HEAD = C.GIT_ATTR_CHECK_INCLUDE_HEAD
    INCLUDE_COMMIT = C.GIT_ATTR_CHECK_INCLUDE_COMMIT


class BlameFlag(IntFlag):
    NORMAL = _pygit2.GIT_BLAME_NORMAL
    "Normal blame, the default"

    TRACK_COPIES_SAME_FILE = _pygit2.GIT_BLAME_TRACK_COPIES_SAME_FILE
    "Not yet implemented and reserved for future use (as of libgit2 1.7.1)."

    TRACK_COPIES_SAME_COMMIT_MOVES = _pygit2.GIT_BLAME_TRACK_COPIES_SAME_COMMIT_MOVES
    "Not yet implemented and reserved for future use (as of libgit2 1.7.1)."

    TRACK_COPIES_SAME_COMMIT_COPIES = _pygit2.GIT_BLAME_TRACK_COPIES_SAME_COMMIT_COPIES
    "Not yet implemented and reserved for future use (as of libgit2 1.7.1)."

    TRACK_COPIES_ANY_COMMIT_COPIES = _pygit2.GIT_BLAME_TRACK_COPIES_ANY_COMMIT_COPIES
    "Not yet implemented and reserved for future use (as of libgit2 1.7.1)."

    FIRST_PARENT = _pygit2.GIT_BLAME_FIRST_PARENT
    "Restrict the search of commits to those reachable following only the first parents."

    USE_MAILMAP = _pygit2.GIT_BLAME_USE_MAILMAP
    """
    Use mailmap file to map author and committer names and email addresses
    to canonical real names and email addresses. The mailmap will be read
    from the working directory, or HEAD in a bare repository.
    """

    IGNORE_WHITESPACE = _pygit2.GIT_BLAME_IGNORE_WHITESPACE
    "Ignore whitespace differences"


class BranchType(IntFlag):
    LOCAL = _pygit2.GIT_BRANCH_LOCAL
    REMOTE = _pygit2.GIT_BRANCH_REMOTE
    ALL = _pygit2.GIT_BRANCH_ALL


class CheckoutNotify(IntFlag):
    """
    Checkout notification flags

    Checkout will invoke an options notification callback
    (`CheckoutCallbacks.checkout_notify`) for certain cases - you pick which
    ones via `CheckoutCallbacks.checkout_notify_flags`.
    """

    NONE = C.GIT_CHECKOUT_NOTIFY_NONE

    CONFLICT = C.GIT_CHECKOUT_NOTIFY_CONFLICT
    "Invokes checkout on conflicting paths."

    DIRTY = C.GIT_CHECKOUT_NOTIFY_DIRTY
    """
    Notifies about "dirty" files, i.e. those that do not need an update
    but no longer match the baseline.  Core git displays these files when
    checkout runs, but won't stop the checkout.
    """

    UPDATED = C.GIT_CHECKOUT_NOTIFY_UPDATED
    "Sends notification for any file changed."

    UNTRACKED = C.GIT_CHECKOUT_NOTIFY_UNTRACKED
    "Notifies about untracked files."

    IGNORED = C.GIT_CHECKOUT_NOTIFY_UNTRACKED
    "Notifies about ignored files."

    ALL = C.GIT_CHECKOUT_NOTIFY_ALL


class CheckoutStrategy(IntFlag):
    NONE = _pygit2.GIT_CHECKOUT_NONE
    "Dry run, no actual updates"

    SAFE = _pygit2.GIT_CHECKOUT_SAFE
    """
    Allow safe updates that cannot overwrite uncommitted data.
    If the uncommitted changes don't conflict with the checked out files,
    the checkout will still proceed, leaving the changes intact.
    
    Mutually exclusive with FORCE.
    FORCE takes precedence over SAFE.
    """

    FORCE = _pygit2.GIT_CHECKOUT_FORCE
    """
    Allow all updates to force working directory to look like index.

    Mutually exclusive with SAFE.
    FORCE takes precedence over SAFE.
    """

    RECREATE_MISSING = _pygit2.GIT_CHECKOUT_RECREATE_MISSING
    """ Allow checkout to recreate missing files """

    ALLOW_CONFLICTS = _pygit2.GIT_CHECKOUT_ALLOW_CONFLICTS
    """ Allow checkout to make safe updates even if conflicts are found """

    REMOVE_UNTRACKED = _pygit2.GIT_CHECKOUT_REMOVE_UNTRACKED
    """ Remove untracked files not in index (that are not ignored) """

    REMOVE_IGNORED = _pygit2.GIT_CHECKOUT_REMOVE_IGNORED
    """ Remove ignored files not in index """

    UPDATE_ONLY = _pygit2.GIT_CHECKOUT_UPDATE_ONLY
    """ Only update existing files, don't create new ones """

    DONT_UPDATE_INDEX = _pygit2.GIT_CHECKOUT_DONT_UPDATE_INDEX
    """
    Normally checkout updates index entries as it goes; this stops that.
    Implies `DONT_WRITE_INDEX`.
    """

    NO_REFRESH = _pygit2.GIT_CHECKOUT_NO_REFRESH
    """ Don't refresh index/config/etc before doing checkout """

    SKIP_UNMERGED = _pygit2.GIT_CHECKOUT_SKIP_UNMERGED
    """ Allow checkout to skip unmerged files """

    USE_OURS = _pygit2.GIT_CHECKOUT_USE_OURS
    """ For unmerged files, checkout stage 2 from index """

    USE_THEIRS = _pygit2.GIT_CHECKOUT_USE_THEIRS
    """ For unmerged files, checkout stage 3 from index """

    DISABLE_PATHSPEC_MATCH = _pygit2.GIT_CHECKOUT_DISABLE_PATHSPEC_MATCH
    """ Treat pathspec as simple list of exact match file paths """

    SKIP_LOCKED_DIRECTORIES = _pygit2.GIT_CHECKOUT_SKIP_LOCKED_DIRECTORIES
    """ Ignore directories in use, they will be left empty """

    DONT_OVERWRITE_IGNORED = _pygit2.GIT_CHECKOUT_DONT_OVERWRITE_IGNORED
    """ Don't overwrite ignored files that exist in the checkout target """

    CONFLICT_STYLE_MERGE = _pygit2.GIT_CHECKOUT_CONFLICT_STYLE_MERGE
    """ Write normal merge files for conflicts """

    CONFLICT_STYLE_DIFF3 = _pygit2.GIT_CHECKOUT_CONFLICT_STYLE_DIFF3
    """ Include common ancestor data in diff3 format files for conflicts """

    DONT_REMOVE_EXISTING = _pygit2.GIT_CHECKOUT_DONT_REMOVE_EXISTING
    """ Don't overwrite existing files or folders """

    DONT_WRITE_INDEX = _pygit2.GIT_CHECKOUT_DONT_WRITE_INDEX
    """ Normally checkout writes the index upon completion; this prevents that. """

    DRY_RUN = _pygit2.GIT_CHECKOUT_DRY_RUN
    """
    Show what would be done by a checkout.  Stop after sending
    notifications; don't update the working directory or index.
    """

    CONFLICT_STYLE_ZDIFF3 = _pygit2.GIT_CHECKOUT_CONFLICT_STYLE_DIFF3
    """ Include common ancestor data in zdiff3 format for conflicts """


class DiffFind(IntFlag):
    """ Flags to control the behavior of diff rename/copy detection. """

    FIND_BY_CONFIG = _pygit2.GIT_DIFF_FIND_BY_CONFIG
    """ Obey `diff.renames`. Overridden by any other FIND_... flag. """

    FIND_RENAMES = _pygit2.GIT_DIFF_FIND_RENAMES
    """ Look for renames? (`--find-renames`) """

    FIND_RENAMES_FROM_REWRITES = _pygit2.GIT_DIFF_FIND_RENAMES_FROM_REWRITES
    """ Consider old side of MODIFIED for renames? (`--break-rewrites=N`) """

    FIND_COPIES = _pygit2.GIT_DIFF_FIND_COPIES
    """ Look for copies? (a la `--find-copies`). """

    FIND_COPIES_FROM_UNMODIFIED = _pygit2.GIT_DIFF_FIND_COPIES_FROM_UNMODIFIED
    """
    Consider UNMODIFIED as copy sources? (`--find-copies-harder`).
    For this to work correctly, use INCLUDE_UNMODIFIED when the initial
    `Diff` is being generated.
    """

    FIND_REWRITES = _pygit2.GIT_DIFF_FIND_REWRITES
    """ Mark significant rewrites for split (`--break-rewrites=/M`) """

    BREAK_REWRITES = _pygit2.GIT_DIFF_BREAK_REWRITES
    """ Actually split large rewrites into delete/add pairs """

    FIND_AND_BREAK_REWRITES = _pygit2.GIT_DIFF_FIND_AND_BREAK_REWRITES
    """ Mark rewrites for split and break into delete/add pairs """

    FIND_FOR_UNTRACKED = _pygit2.GIT_DIFF_FIND_FOR_UNTRACKED
    """
    Find renames/copies for UNTRACKED items in working directory.
    For this to work correctly, use INCLUDE_UNTRACKED when the initial
    `Diff` is being generated (and obviously the diff must be against
    the working directory for this to make sense).
    """

    FIND_ALL = _pygit2.GIT_DIFF_FIND_ALL
    """ Turn on all finding features. """

    FIND_IGNORE_LEADING_WHITESPACE = _pygit2.GIT_DIFF_FIND_IGNORE_LEADING_WHITESPACE
    """ Measure similarity ignoring leading whitespace (default) """

    FIND_IGNORE_WHITESPACE = _pygit2.GIT_DIFF_FIND_IGNORE_WHITESPACE
    """ Measure similarity ignoring all whitespace """

    FIND_DONT_IGNORE_WHITESPACE = _pygit2.GIT_DIFF_FIND_DONT_IGNORE_WHITESPACE
    """ Measure similarity including all data """

    FIND_EXACT_MATCH_ONLY = _pygit2.GIT_DIFF_FIND_EXACT_MATCH_ONLY
    """ Measure similarity only by comparing SHAs (fast and cheap) """

    BREAK_REWRITES_FOR_RENAMES_ONLY = _pygit2.GIT_DIFF_BREAK_REWRITES_FOR_RENAMES_ONLY
    """
    Do not break rewrites unless they contribute to a rename.

    Normally, FIND_AND_BREAK_REWRITES will measure the self-
    similarity of modified files and split the ones that have changed a
    lot into a DELETE / ADD pair.  Then the sides of that pair will be
    considered candidates for rename and copy detection.

    If you add this flag in and the split pair is *not* used for an
    actual rename or copy, then the modified record will be restored to
    a regular MODIFIED record instead of being split.
    """

    FIND_REMOVE_UNMODIFIED = _pygit2.GIT_DIFF_FIND_REMOVE_UNMODIFIED
    """
    Remove any UNMODIFIED deltas after find_similar is done.

    Using FIND_COPIES_FROM_UNMODIFIED to emulate the
    --find-copies-harder behavior requires building a diff with the
    INCLUDE_UNMODIFIED flag.  If you do not want UNMODIFIED records
    in the final result, pass this flag to have them removed.
    """


class DiffOption(IntFlag):
    """
    Flags for diff options.  A combination of these flags can be passed
    in via the `flags` value in `diff_*` functions.
    """

    NORMAL = _pygit2.GIT_DIFF_NORMAL
    "Normal diff, the default"

    REVERSE = _pygit2.GIT_DIFF_REVERSE
    "Reverse the sides of the diff"

    INCLUDE_IGNORED = _pygit2.GIT_DIFF_INCLUDE_IGNORED
    "Include ignored files in the diff"

    RECURSE_IGNORED_DIRS = _pygit2.GIT_DIFF_RECURSE_IGNORED_DIRS
    """
    Even with INCLUDE_IGNORED, an entire ignored directory
    will be marked with only a single entry in the diff; this flag
    adds all files under the directory as IGNORED entries, too.
    """

    INCLUDE_UNTRACKED = _pygit2.GIT_DIFF_INCLUDE_UNTRACKED
    "Include untracked files in the diff"

    RECURSE_UNTRACKED_DIRS = _pygit2.GIT_DIFF_RECURSE_UNTRACKED_DIRS
    """
    Even with INCLUDE_UNTRACKED, an entire untracked
    directory will be marked with only a single entry in the diff
    (a la what core Git does in `git status`); this flag adds *all*
    files under untracked directories as UNTRACKED entries, too.
    """

    INCLUDE_UNMODIFIED = _pygit2.GIT_DIFF_INCLUDE_UNMODIFIED
    "Include unmodified files in the diff"

    INCLUDE_TYPECHANGE = _pygit2.GIT_DIFF_INCLUDE_TYPECHANGE
    """
    Normally, a type change between files will be converted into a
    DELETED record for the old and an ADDED record for the new; this
    options enabled the generation of TYPECHANGE delta records.
    """

    INCLUDE_TYPECHANGE_TREES = _pygit2.GIT_DIFF_INCLUDE_TYPECHANGE_TREES
    """
    Even with INCLUDE_TYPECHANGE, blob->tree changes still generally
    show as a DELETED blob.  This flag tries to correctly label
    blob->tree transitions as TYPECHANGE records with new_file's
    mode set to tree.  Note: the tree SHA will not be available.
    """

    IGNORE_FILEMODE = _pygit2.GIT_DIFF_IGNORE_FILEMODE
    "Ignore file mode changes"

    IGNORE_SUBMODULES = _pygit2.GIT_DIFF_IGNORE_SUBMODULES
    "Treat all submodules as unmodified"

    IGNORE_CASE = _pygit2.GIT_DIFF_IGNORE_CASE
    "Use case insensitive filename comparisons"

    INCLUDE_CASECHANGE = _pygit2.GIT_DIFF_INCLUDE_CASECHANGE
    """
    May be combined with IGNORE_CASE to specify that a file
    that has changed case will be returned as an add/delete pair.
    """

    DISABLE_PATHSPEC_MATCH = _pygit2.GIT_DIFF_DISABLE_PATHSPEC_MATCH
    """
    If the pathspec is set in the diff options, this flags indicates
    that the paths will be treated as literal paths instead of
    fnmatch patterns.  Each path in the list must either be a full
    path to a file or a directory.  (A trailing slash indicates that
    the path will _only_ match a directory).  If a directory is
    specified, all children will be included.
    """

    SKIP_BINARY_CHECK = _pygit2.GIT_DIFF_SKIP_BINARY_CHECK
    """
    Disable updating of the `binary` flag in delta records.  This is
    useful when iterating over a diff if you don't need hunk and data
    callbacks and want to avoid having to load file completely.
    """

    ENABLE_FAST_UNTRACKED_DIRS = _pygit2.GIT_DIFF_ENABLE_FAST_UNTRACKED_DIRS
    """
    When diff finds an untracked directory, to match the behavior of
    core Git, it scans the contents for IGNORED and UNTRACKED files.
    If *all* contents are IGNORED, then the directory is IGNORED; if
    any contents are not IGNORED, then the directory is UNTRACKED.
    This is extra work that may not matter in many cases.  This flag
    turns off that scan and immediately labels an untracked directory
    as UNTRACKED (changing the behavior to not match core Git).
    """

    UPDATE_INDEX = _pygit2.GIT_DIFF_UPDATE_INDEX
    """
    When diff finds a file in the working directory with stat
    information different from the index, but the OID ends up being the
    same, write the correct stat information into the index.  Note:
    without this flag, diff will always leave the index untouched.
    """

    INCLUDE_UNREADABLE = _pygit2.GIT_DIFF_INCLUDE_UNREADABLE
    "Include unreadable files in the diff"

    INCLUDE_UNREADABLE_AS_UNTRACKED = _pygit2.GIT_DIFF_INCLUDE_UNREADABLE_AS_UNTRACKED
    "Include unreadable files in the diff"

    INDENT_HEURISTIC = _pygit2.GIT_DIFF_INDENT_HEURISTIC
    """
    Use a heuristic that takes indentation and whitespace into account
    which generally can produce better diffs when dealing with ambiguous
    diff hunks.
    """

    IGNORE_BLANK_LINES = _pygit2.GIT_DIFF_IGNORE_BLANK_LINES
    "Ignore blank lines"

    FORCE_TEXT = _pygit2.GIT_DIFF_FORCE_TEXT
    "Treat all files as text, disabling binary attributes & detection"

    FORCE_BINARY = _pygit2.GIT_DIFF_FORCE_BINARY
    "Treat all files as binary, disabling text diffs"

    IGNORE_WHITESPACE = _pygit2.GIT_DIFF_IGNORE_WHITESPACE
    "Ignore all whitespace"

    IGNORE_WHITESPACE_CHANGE = _pygit2.GIT_DIFF_IGNORE_WHITESPACE_CHANGE
    "Ignore changes in amount of whitespace"

    IGNORE_WHITESPACE_EOL = _pygit2.GIT_DIFF_IGNORE_WHITESPACE_EOL
    "Ignore whitespace at end of line"

    SHOW_UNTRACKED_CONTENT = _pygit2.GIT_DIFF_SHOW_UNTRACKED_CONTENT
    """
    When generating patch text, include the content of untracked files.
    This automatically turns on INCLUDE_UNTRACKED but it does not turn
    on RECURSE_UNTRACKED_DIRS.  Add that flag if you want the content
    of every single UNTRACKED file.
    """

    SHOW_UNMODIFIED = _pygit2.GIT_DIFF_SHOW_UNMODIFIED
    """
    When generating output, include the names of unmodified files if
    they are included in the git_diff.  Normally these are skipped in
    the formats that list files (e.g. name-only, name-status, raw).
    Even with this, these will not be included in patch format.
    """

    PATIENCE = _pygit2.GIT_DIFF_PATIENCE
    "Use the 'patience diff' algorithm"

    MINIMAL = _pygit2.GIT_DIFF_MINIMAL
    "Take extra time to find minimal diff"

    SHOW_BINARY = _pygit2.GIT_DIFF_SHOW_BINARY
    """
    Include the necessary deflate / delta information so that `git-apply`
    can apply given diff information to binary files.
    """


class Feature(IntFlag):
    """
    Combinations of these values describe the features with which libgit2
    was compiled.
    """

    THREADS = C.GIT_FEATURE_THREADS
    HTTPS = C.GIT_FEATURE_HTTPS
    SSH = C.GIT_FEATURE_SSH
    NSEC = C.GIT_FEATURE_NSEC


class FileMode(IntFlag):
    UNREADABLE = _pygit2.GIT_FILEMODE_UNREADABLE
    TREE = _pygit2.GIT_FILEMODE_TREE
    BLOB = _pygit2.GIT_FILEMODE_BLOB
    BLOB_EXECUTABLE = _pygit2.GIT_FILEMODE_BLOB_EXECUTABLE
    LINK = _pygit2.GIT_FILEMODE_LINK
    COMMIT = _pygit2.GIT_FILEMODE_COMMIT


class MergeAnalysis(IntFlag):
    """ The results of `Repository.merge_analysis` indicate the merge opportunities. """

    NONE = _pygit2.GIT_MERGE_ANALYSIS_NONE
    "No merge is possible.  (Unused.)"

    NORMAL = _pygit2.GIT_MERGE_ANALYSIS_NORMAL
    """
    A "normal" merge; both HEAD and the given merge input have diverged
    from their common ancestor.  The divergent commits must be merged.
    """

    UP_TO_DATE = _pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE
    """
    All given merge inputs are reachable from HEAD, meaning the
    repository is up-to-date and no merge needs to be performed.
    """

    FASTFORWARD = _pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD
    """
    The given merge input is a fast-forward from HEAD and no merge
    needs to be performed.  Instead, the client can check out the
    given merge input.
    """

    UNBORN = _pygit2.GIT_MERGE_ANALYSIS_UNBORN
    """
    The HEAD of the current repository is "unborn" and does not point to
    a valid commit.  No merge can be performed, but the caller may wish
    to simply set HEAD to the target commit(s).
    """


class MergePreference(IntFlag):
    """ The user's stated preference for merges. """

    NONE = _pygit2.GIT_MERGE_PREFERENCE_NONE
    "No configuration was found that suggests a preferred behavior for merge."

    NO_FASTFORWARD = _pygit2.GIT_MERGE_PREFERENCE_NO_FASTFORWARD
    """
    There is a `merge.ff=false` configuration setting, suggesting that
    the user does not want to allow a fast-forward merge.
    """

    FASTFORWARD_ONLY = _pygit2.GIT_MERGE_PREFERENCE_FASTFORWARD_ONLY
    """
    There is a `merge.ff=only` configuration setting, suggesting that
    the user only wants fast-forward merges.
    """


class Option(IntEnum):
    """ Global libgit2 library options """
    # Commented out values --> exists in libgit2 but not supported in pygit2's options.c yet
    GET_MWINDOW_SIZE = _pygit2.GIT_OPT_GET_MWINDOW_SIZE
    SET_MWINDOW_SIZE = _pygit2.GIT_OPT_SET_MWINDOW_SIZE
    GET_MWINDOW_MAPPED_LIMIT = _pygit2.GIT_OPT_GET_MWINDOW_MAPPED_LIMIT
    SET_MWINDOW_MAPPED_LIMIT = _pygit2.GIT_OPT_SET_MWINDOW_MAPPED_LIMIT
    GET_SEARCH_PATH = _pygit2.GIT_OPT_GET_SEARCH_PATH
    SET_SEARCH_PATH = _pygit2.GIT_OPT_SET_SEARCH_PATH
    SET_CACHE_OBJECT_LIMIT = _pygit2.GIT_OPT_SET_CACHE_OBJECT_LIMIT
    SET_CACHE_MAX_SIZE = _pygit2.GIT_OPT_SET_CACHE_MAX_SIZE
    ENABLE_CACHING = _pygit2.GIT_OPT_ENABLE_CACHING
    GET_CACHED_MEMORY = _pygit2.GIT_OPT_GET_CACHED_MEMORY
    GET_TEMPLATE_PATH = _pygit2.GIT_OPT_GET_TEMPLATE_PATH
    SET_TEMPLATE_PATH = _pygit2.GIT_OPT_SET_TEMPLATE_PATH
    SET_SSL_CERT_LOCATIONS = _pygit2.GIT_OPT_SET_SSL_CERT_LOCATIONS
    SET_USER_AGENT = _pygit2.GIT_OPT_SET_USER_AGENT
    ENABLE_STRICT_OBJECT_CREATION = _pygit2.GIT_OPT_ENABLE_STRICT_OBJECT_CREATION
    ENABLE_STRICT_SYMBOLIC_REF_CREATION = _pygit2.GIT_OPT_ENABLE_STRICT_SYMBOLIC_REF_CREATION
    SET_SSL_CIPHERS = _pygit2.GIT_OPT_SET_SSL_CIPHERS
    GET_USER_AGENT = _pygit2.GIT_OPT_GET_USER_AGENT
    ENABLE_OFS_DELTA = _pygit2.GIT_OPT_ENABLE_OFS_DELTA
    ENABLE_FSYNC_GITDIR = _pygit2.GIT_OPT_ENABLE_FSYNC_GITDIR
    GET_WINDOWS_SHAREMODE = _pygit2.GIT_OPT_GET_WINDOWS_SHAREMODE
    SET_WINDOWS_SHAREMODE = _pygit2.GIT_OPT_SET_WINDOWS_SHAREMODE
    ENABLE_STRICT_HASH_VERIFICATION = _pygit2.GIT_OPT_ENABLE_STRICT_HASH_VERIFICATION
    SET_ALLOCATOR = _pygit2.GIT_OPT_SET_ALLOCATOR
    ENABLE_UNSAVED_INDEX_SAFETY = _pygit2.GIT_OPT_ENABLE_UNSAVED_INDEX_SAFETY
    GET_PACK_MAX_OBJECTS = _pygit2.GIT_OPT_GET_PACK_MAX_OBJECTS
    SET_PACK_MAX_OBJECTS = _pygit2.GIT_OPT_SET_PACK_MAX_OBJECTS
    DISABLE_PACK_KEEP_FILE_CHECKS = _pygit2.GIT_OPT_DISABLE_PACK_KEEP_FILE_CHECKS
    # ENABLE_HTTP_EXPECT_CONTINUE = _pygit2.GIT_OPT_ENABLE_HTTP_EXPECT_CONTINUE
    # GET_MWINDOW_FILE_LIMIT = _pygit2.GIT_OPT_GET_MWINDOW_FILE_LIMIT
    # SET_MWINDOW_FILE_LIMIT = _pygit2.GIT_OPT_SET_MWINDOW_FILE_LIMIT
    # SET_ODB_PACKED_PRIORITY = _pygit2.GIT_OPT_SET_ODB_PACKED_PRIORITY
    # SET_ODB_LOOSE_PRIORITY = _pygit2.GIT_OPT_SET_ODB_LOOSE_PRIORITY
    # GET_EXTENSIONS = _pygit2.GIT_OPT_GET_EXTENSIONS
    # SET_EXTENSIONS = _pygit2.GIT_OPT_SET_EXTENSIONS
    GET_OWNER_VALIDATION = _pygit2.GIT_OPT_GET_OWNER_VALIDATION
    SET_OWNER_VALIDATION = _pygit2.GIT_OPT_SET_OWNER_VALIDATION
    # GET_HOMEDIR = _pygit2.GIT_OPT_GET_HOMEDIR
    # SET_HOMEDIR = _pygit2.GIT_OPT_SET_HOMEDIR
    # SET_SERVER_CONNECT_TIMEOUT = _pygit2.GIT_OPT_SET_SERVER_CONNECT_TIMEOUT
    # GET_SERVER_CONNECT_TIMEOUT = _pygit2.GIT_OPT_GET_SERVER_CONNECT_TIMEOUT
    # SET_SERVER_TIMEOUT = _pygit2.GIT_OPT_SET_SERVER_TIMEOUT
    # GET_SERVER_TIMEOUT = _pygit2.GIT_OPT_GET_SERVER_TIMEOUT


class ReferenceFilter(IntEnum):
    """ Filters for References.iterator(). """

    ALL = _pygit2.GIT_REFERENCES_ALL
    BRANCHES = _pygit2.GIT_REFERENCES_BRANCHES
    TAGS = _pygit2.GIT_REFERENCES_TAGS


class ReferenceType(IntFlag):
    """ Basic type of any Git reference. """

    INVALID = _pygit2.GIT_REF_INVALID
    OID = _pygit2.GIT_REF_OID
    SYMBOLIC = _pygit2.GIT_REF_SYMBOLIC
    LISTALL = _pygit2.GIT_REF_LISTALL


class RepositoryInitFlag(IntFlag):
    """
    Option flags for pygit2.init_repository().
    """

    BARE = C.GIT_REPOSITORY_INIT_BARE
    "Create a bare repository with no working directory."

    NO_REINIT = C.GIT_REPOSITORY_INIT_NO_REINIT
    "Raise GitError if the path appears to already be a git repository."

    NO_DOTGIT_DIR = C.GIT_REPOSITORY_INIT_NO_DOTGIT_DIR
    """Normally a "/.git/" will be appended to the repo path for
    non-bare repos (if it is not already there), but passing this flag
    prevents that behavior."""

    MKDIR = C.GIT_REPOSITORY_INIT_MKDIR
    """Make the repo_path (and workdir_path) as needed. Init is always willing
    to create the ".git" directory even without this flag. This flag tells
    init to create the trailing component of the repo and workdir paths
    as needed."""

    MKPATH = C.GIT_REPOSITORY_INIT_MKPATH
    "Recursively make all components of the repo and workdir paths as necessary."

    EXTERNAL_TEMPLATE = C.GIT_REPOSITORY_INIT_EXTERNAL_TEMPLATE
    """libgit2 normally uses internal templates to initialize a new repo.
    This flags enables external templates, looking at the "template_path" from
    the options if set, or the `init.templatedir` global config if not,
    or falling back on "/usr/share/git-core/templates" if it exists."""

    RELATIVE_GITLINK = C.GIT_REPOSITORY_INIT_RELATIVE_GITLINK
    """If an alternate workdir is specified, use relative paths for the gitdir
    and core.worktree."""


class RepositoryInitMode(IntEnum):
    """
    Mode options for pygit2.init_repository().
    """

    SHARED_UMASK = C.GIT_REPOSITORY_INIT_SHARED_UMASK
    "Use permissions configured by umask - the default."

    SHARED_GROUP = C.GIT_REPOSITORY_INIT_SHARED_GROUP
    """
    Use '--shared=group' behavior, chmod'ing the new repo to be group
    writable and "g+sx" for sticky group assignment.
    """

    SHARED_ALL = C.GIT_REPOSITORY_INIT_SHARED_ALL
    "Use '--shared=all' behavior, adding world readability."


class RepositoryOpenFlag(IntFlag):
    """
    Option flags for Repository.__init__().
    """

    DEFAULT = 0
    "Default flags."

    NO_SEARCH = C.GIT_REPOSITORY_OPEN_NO_SEARCH
    """
    Only open the repository if it can be immediately found in the
    start_path. Do not walk up from the start_path looking at parent
    directories.
    """

    CROSS_FS = C.GIT_REPOSITORY_OPEN_CROSS_FS
    """
    Unless this flag is set, open will not continue searching across
    filesystem boundaries (i.e. when `st_dev` changes from the `stat`
    system call).  For example, searching in a user's home directory at
    "/home/user/source/" will not return "/.git/" as the found repo if
    "/" is a different filesystem than "/home".
    """

    BARE = C.GIT_REPOSITORY_OPEN_BARE
    """
    Open repository as a bare repo regardless of core.bare config, and
    defer loading config file for faster setup.
    Unlike `git_repository_open_bare`, this can follow gitlinks.
    """

    NO_DOTGIT = C.GIT_REPOSITORY_OPEN_NO_DOTGIT
    """
    Do not check for a repository by appending /.git to the start_path;
    only open the repository if start_path itself points to the git
    directory.
    """

    FROM_ENV = C.GIT_REPOSITORY_OPEN_FROM_ENV
    """
    Find and open a git repository, respecting the environment variables
    used by the git command-line tools.
    If set, `git_repository_open_ext` will ignore the other flags and
    the `ceiling_dirs` argument, and will allow a NULL `path` to use
    `GIT_DIR` or search from the current directory.
    The search for a repository will respect $GIT_CEILING_DIRECTORIES and
    $GIT_DISCOVERY_ACROSS_FILESYSTEM.  The opened repository will
    respect $GIT_INDEX_FILE, $GIT_NAMESPACE, $GIT_OBJECT_DIRECTORY, and
    $GIT_ALTERNATE_OBJECT_DIRECTORIES.
    In the future, this flag will also cause `git_repository_open_ext`
    to respect $GIT_WORK_TREE and $GIT_COMMON_DIR; currently,
    `git_repository_open_ext` with this flag will error out if either
    $GIT_WORK_TREE or $GIT_COMMON_DIR is set.
    """


class RepositoryState(IntEnum):
    """
    Repository state: These values represent possible states for the repository
    to be in, based on the current operation which is ongoing.
    """
    NONE = C.GIT_REPOSITORY_STATE_NONE
    MERGE = C.GIT_REPOSITORY_STATE_MERGE
    REVERT = C.GIT_REPOSITORY_STATE_REVERT
    REVERT_SEQUENCE = C.GIT_REPOSITORY_STATE_REVERT_SEQUENCE
    CHERRYPICK = C.GIT_REPOSITORY_STATE_CHERRYPICK
    CHERRYPICK_SEQUENCE = C.GIT_REPOSITORY_STATE_CHERRYPICK_SEQUENCE
    BISECT = C.GIT_REPOSITORY_STATE_BISECT
    REBASE = C.GIT_REPOSITORY_STATE_REBASE
    REBASE_INTERACTIVE = C.GIT_REPOSITORY_STATE_REBASE_INTERACTIVE
    REBASE_MERGE = C.GIT_REPOSITORY_STATE_REBASE_MERGE
    APPLY_MAILBOX = C.GIT_REPOSITORY_STATE_APPLY_MAILBOX
    APPLY_MAILBOX_OR_REBASE = C.GIT_REPOSITORY_STATE_APPLY_MAILBOX_OR_REBASE


class ResetMode(IntEnum):
    """ Kinds of reset operation. """

    SOFT = _pygit2.GIT_RESET_SOFT
    "Move the head to the given commit"

    MIXED = _pygit2.GIT_RESET_MIXED
    "SOFT plus reset index to the commit"

    HARD = _pygit2.GIT_RESET_HARD
    "MIXED plus changes in working tree discarded"


class SortMode(IntFlag):
    """
    Flags to specify the sorting which a revwalk should perform.
    """

    NONE = _pygit2.GIT_SORT_NONE
    """
    Sort the output with the same default method from `git`: reverse
    chronological order. This is the default sorting for new walkers.
    """

    TOPOLOGICAL = _pygit2.GIT_SORT_TOPOLOGICAL
    """
    Sort the repository contents in topological order (no parents before
    all of its children are shown); this sorting mode can be combined
    with TIME sorting to produce `git`'s `--date-order``.
    """

    TIME = _pygit2.GIT_SORT_TIME
    """
    Sort the repository contents by commit time; this sorting mode can be
    combined with TOPOLOGICAL.
    """

    REVERSE = _pygit2.GIT_SORT_REVERSE
    """
    Iterate through the repository contents in reverse order;
    this sorting mode can be combined with any of the above.
    """


class StashApplyProgress(IntEnum):
    """
    Stash apply progression states
    """

    NONE = C.GIT_STASH_APPLY_PROGRESS_NONE

    LOADING_STASH = C.GIT_STASH_APPLY_PROGRESS_LOADING_STASH
    "Loading the stashed data from the object database."

    ANALYZE_INDEX = C.GIT_STASH_APPLY_PROGRESS_ANALYZE_INDEX
    "The stored index is being analyzed."

    ANALYZE_MODIFIED = C.GIT_STASH_APPLY_PROGRESS_ANALYZE_MODIFIED
    "The modified files are being analyzed."

    ANALYZE_UNTRACKED = C.GIT_STASH_APPLY_PROGRESS_ANALYZE_UNTRACKED
    "The untracked and ignored files are being analyzed."

    CHECKOUT_UNTRACKED = C.GIT_STASH_APPLY_PROGRESS_CHECKOUT_UNTRACKED
    "The untracked files are being written to disk."

    CHECKOUT_MODIFIED = C.GIT_STASH_APPLY_PROGRESS_CHECKOUT_MODIFIED
    "The modified files are being written to disk."

    DONE = C.GIT_STASH_APPLY_PROGRESS_DONE
    "The stash was applied successfully."


class SubmoduleIgnore(IntEnum):
    UNSPECIFIED = _pygit2.GIT_SUBMODULE_IGNORE_UNSPECIFIED
    "use the submodule's configuration"

    NONE = _pygit2.GIT_SUBMODULE_IGNORE_NONE
    "any change or untracked == dirty"

    UNTRACKED = _pygit2.GIT_SUBMODULE_IGNORE_UNTRACKED
    "dirty if tracked files change"

    DIRTY = _pygit2.GIT_SUBMODULE_IGNORE_DIRTY
    "only dirty if HEAD moved"

    ALL = _pygit2.GIT_SUBMODULE_IGNORE_ALL
    "never dirty"


class SubmoduleStatus(IntFlag):
    IN_HEAD = _pygit2.GIT_SUBMODULE_STATUS_IN_HEAD
    "superproject head contains submodule"

    IN_INDEX = _pygit2.GIT_SUBMODULE_STATUS_IN_INDEX
    "superproject index contains submodule"

    IN_CONFIG = _pygit2.GIT_SUBMODULE_STATUS_IN_CONFIG
    "superproject gitmodules has submodule"

    IN_WD = _pygit2.GIT_SUBMODULE_STATUS_IN_WD
    "superproject workdir has submodule"

    INDEX_ADDED = _pygit2.GIT_SUBMODULE_STATUS_INDEX_ADDED
    "in index, not in head (flag available if ignore is not ALL)"

    INDEX_DELETED = _pygit2.GIT_SUBMODULE_STATUS_INDEX_DELETED
    "in head, not in index (flag available if ignore is not ALL)"

    INDEX_MODIFIED = _pygit2.GIT_SUBMODULE_STATUS_INDEX_MODIFIED
    "index and head don't match (flag available if ignore is not ALL)"

    WD_UNINITIALIZED = _pygit2.GIT_SUBMODULE_STATUS_WD_UNINITIALIZED
    "workdir contains empty repository (flag available if ignore is not ALL)"

    WD_ADDED = _pygit2.GIT_SUBMODULE_STATUS_WD_ADDED
    "in workdir, not index (flag available if ignore is not ALL)"

    WD_DELETED = _pygit2.GIT_SUBMODULE_STATUS_WD_DELETED
    "in index, not workdir (flag available if ignore is not ALL)"

    WD_MODIFIED = _pygit2.GIT_SUBMODULE_STATUS_WD_MODIFIED
    "index and workdir head don't match (flag available if ignore is not ALL)"

    WD_INDEX_MODIFIED = _pygit2.GIT_SUBMODULE_STATUS_WD_INDEX_MODIFIED
    "submodule workdir index is dirty (flag available if ignore is NONE or UNTRACKED)"

    WD_WD_MODIFIED = _pygit2.GIT_SUBMODULE_STATUS_WD_WD_MODIFIED
    "submodule workdir has modified files (flag available if ignore is NONE or UNTRACKED)"

    WD_UNTRACKED = _pygit2.GIT_SUBMODULE_STATUS_WD_UNTRACKED
    "submodule workdir contains untracked files (flag available if ignore is NONE)"
