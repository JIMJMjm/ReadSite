# Change Log

## [0.2.0] 2026-03-22

### What's New
- Recommendation system is now available. Users can aquire `Recos` through daily check-in and use them to recommend a book in its detail page.
- The display of recommended book on title page has a revamped logic.

### Bug Fixes
- Fixed `UserPoint not exist` when trying to download books via a pre-registed User.

### Improvements
- Added `library` link to book detail page.

### Future Features
- [ ] Custom order criteria, filters and book groups.
- [x] Recommendation system.


## [0.1.2] 2026-03-20

### What's New
- A book can now only bound to 6 tags.
- Changed book_download view & API view, now a book with illustrations will be downloaded as a .zip file.

### Bug Fixes
- Fixed the CSRF-verification error caused by `settings.py` on server.

### Improvements
- Added `我的书架` link to library page.

### Future Features
- [x] Set a maximum for tags of each book.
- [ ] Custom order criteria, filters and book groups.
- [ ] Recommendation system.