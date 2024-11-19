# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
and the format of this file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).


## [0.5.0] - 2024-11-19

### Added
- Paging support for to all operations whose paths end with _list .

### Changed
- Upgraded Lapidary to 0.12.0 .
- Updated GSMTasks OpenAPI to 2.4.42 .
- Removed /gen/ directory from .gitignore .
- Changed license to only 0BSD.

### Fixed
- Serialization style for parameters ending with __in and __not_in and _or_null
- Format for date parameters and types for __is_null, id and duration parameters.


## [0.4.0] - 2022-12-15
### Changed
- Removed dependency on lapidary generator.
- Updated lapidary to 0.7.2
- Updated GSMTasks OpenAPI to 2.4.13


## [0.3.0](https://github.com/oeklo/gsmtasks-client/releases/tag/v0.3.0) - 2022-10-27
### Added
- taskipy and a task to update code with lapidary

### Changed
- Upgraded lapidary to 0.6.1
- migrated from APIKey auth to Token
- Changed some enum keys


## [0.2.1](https://github.com/oeklo/gsmtasks-client/releases/tag/v0.2.1) - 2022-10-21
### Changed
- Upgraded lapidary
- Split errata into smaller files

### Fixed
- nullability of some properties


## [0.2.0](https://github.com/oeklo/gsmtasks-client/releases/tag/v0.2.0) - 2022-10-17
## Added
- enums
- non-required properties

## Changed
- client is now an async context manager
- methods are now sorted

## Fixed
- int constraints

## [0.1.0]
### Changed
- New code generated with Lapidary


## [0.0.1](https://github.com/oeklo/gsmtasks-client/releases/tag/v0.0.1) - 2022-04-29


[Unreleased]: https://github.com/lapidary-library/gsmtasks/-/compare/v0.5.0...HEAD
[0.5.0]:      https://github.com/lapidary-library/gsmtasks/-/compare/v0.4.0...v0.5.0
[0.4.0]:      https://github.com/lapidary-library/gsmtasks/-/compare/v0.3.0...v0.4.0
