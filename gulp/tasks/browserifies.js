/**
 * Dependencies
 */
const path = require('path');
const browserify = require('browserify');
const babelify = require('babelify');
const source = require('vinyl-source-stream');
const gulp = require('gulp');

/**
 * Module body / Expose
 */
module.exports = (entries, config, dist) => {
    //  config = config || {};
    //  // I add config to browserify(entry) 
    //  const built = browserify(entry, config)
    //    .transform(babelify);
    //  return built.bundle().pipe(source(path.basename(entry)));

    // var t_built;
    // handle many js files
    entries = entries || [];
    config = config || {};

    for (var entry of entries) {
        var t_built = browserify(entry, config).transform(babelify);
        t_built.bundle().pipe(source(path.basename(entry))).pipe(gulp.dest(dist));
    }

    // entries.forEach(function (entry) {
    //  let t_built = browserify(entry, config).transform(babelify);
    //  t_built.bundle().pipe(source(path.basename(entry))); 
    // });
    return;
};