/**
 * Setup
 */
process.title = process.title || 'gulp';

/**
 * Dependencies
 */
const path = require('path');
const gulp = require('gulp');

/**
 * Setup
 */
const tasks = require(path.resolve(__dirname, 'gulp/tasks'));
const config = require(path.resolve(__dirname, 'gulp/config'));
// console.log(config);

/**
 * Tasks
 */
gulp.task('build:clean', function buildClean() {
    tasks.clean(config.paths.build);
    return tasks.clean(config.paths.dist);
});

gulp.task('build:styles', function buildStyles() {
    return tasks.css(config.styles.source, { less: { paths: config.styles.npmPaths } })
        .pipe(gulp.dest(config.styles.dist));
});

// only for site.js
gulp.task('build:js', function buildJS() {
    return tasks.browserify(config.scripts.main)
        .pipe(gulp.dest(config.scripts.dist));
});

// only for bpmnshow.js
gulp.task('build:bpmnjs', function buildJS() {
    return tasks.browserify(config.scripts.bpmnjs, {
            debug: true,
            list: true,
            // make sure we do not include browser shims unnecessarily
            insertGlobalVars: {
                process: function() {
                    return 'undefined';
                },
                Buffer: function() {
                    return 'undefined';
                }
            },
            transform: ['brfs']
        })
        .pipe(gulp.dest(config.scripts.dist));
});

// necessary task for bpmnshow.js
// gulp.task('build:browserify', function buildBrowserify() {
// return browserify('./static/src/js/bpmnshow.js')
// .bundle()
// .pipe(source('bundle.js'))
// .pipe(gulp.dest(config.scripts.dist));
// });


gulp.task('manifest', function manifest() {
    return tasks.rev(config.manifest.source)
        .pipe(gulp.dest(config.paths.dist))
        .pipe(tasks.manifest())
        .pipe(gulp.dest(config.paths.build));
});

gulp.task('build:copy-icons', function() { 
    return tasks.copy(config.fonts.sources)
        .pipe(gulp.dest(config.fonts.dist)); 
});
gulp.task('build:copy-images', function() {
    return tasks.copy(config.images.sources).pipe(gulp.dest(config.images.dist));
});
gulp.task('build:copy-less', function() {
    return tasks.copy(config.less.sources).pipe(gulp.dest(config.less.dist));
});

gulp.task('build:script-include', function() {
    // tasks.handlebars(config.templates.manifestPath, config.templates.bpmn_scriptsTemplate, config.staticUrlRoot)
    //     .pipe(gulp.dest(config.templates.bpmn_des));
    tasks.handlebars(config.templates.manifestPath, config.templates.bpmn_scriptsTemplate, config.staticUrlRoot)
        .pipe(gulp.dest(config.templates.destination));  
    return tasks.handlebars(config.templates.manifestPath, config.templates.scriptsTemplate, config.staticUrlRoot)
        .pipe(gulp.dest(config.templates.destination));    
});

gulp.task('build:style-include', function() {
    return tasks.handlebars(config.templates.manifestPath, config.templates.stylesTemplate, config.staticUrlRoot)
        .pipe(gulp.dest(config.templates.destination));
});

gulp.task('test', function test() {
    return tasks.test(config.test.all);
});

gulp.task('test:req', function testReq() {
    return tasks.test(config.test.req);
});

gulp.task('test:components', function testComponents() {
    return tasks.test(config.test.components);
});

// gulp.task('xo', function xo() {
// return tasks.xo(config.xo.source);
// });

gulp.task('optimize:js', function() {
    return tasks.optimizejs(config.optimize.js.source, config.optimize.js.options, config.optimize.js.dist);
});

gulp.task('optimize:css', function() {
    return tasks.optimizecss(config.optimize.css.source, config.optimize.css.options, config.optimize.css.dist);
});

/**
 * Compound Tasks
 * add watch bpmnjs
 */
gulp.task('watch', function watch() {
    gulp.watch(config.watch.styles, gulp.series(['build:styles', 'manifest', 'build:style-include']));
    gulp.watch(config.watch.scripts, gulp.series(['build:js', 'manifest', 'build:script-include']));
    gulp.watch(config.watch.scripts, gulp.series(['build:bpmnjs', 'manifest', 'build:script-include']));
});

gulp.task('build', gulp.series([
    // 'xo',
    'build:clean',
    gulp.parallel([
        'build:styles',
        'build:js',
        'build:bpmnjs',
        'build:copy-icons',
        'build:copy-images',
        'build:copy-less'
    ]),
    'manifest',
    'build:script-include',
    'build:style-include'
]));

gulp.task('default', gulp.series([
    'build',
    'watch'
]));

gulp.task('release', gulp.series([
    'build',
    'optimize:js',
    'optimize:css'
]));