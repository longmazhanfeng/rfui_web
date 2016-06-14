/**
 * Dependencies
 */
const path = require('path');
const browserify = require('browserify');
const babelify   = require('babelify');
const source     = require('vinyl-source-stream');

/**
 * Module body / Expose
 */
module.exports = (entry, config) => {
  config = config || {};
  // I add config to browserify(entry) 
  const built = browserify(entry, config)
    .transform(babelify);
  return built.bundle().pipe(source(path.basename(entry)));
};
