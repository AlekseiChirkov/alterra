const gulp = require('gulp');
const gulp_sass = require('gulp-sass');

function sass_to_css() {
    return gulp.src('../scss/**/*.scss')
        .pipe(gulp_sass())
        .pipe(gulp.dest('../css'));
}

function watch() {
    gulp.watch('../scss/**/*.scss', sass_to_css);
}

exports.style = sass_to_css;
exports.watch = watch;