const templatePath = 'myaccoutsite/templates/';
const staticRoot = 'static/';
const staticSource = staticRoot + 'src/';
const staticBuild = staticRoot + '_build/';
const staticDist = staticRoot + 'dist/';
const npmRoot = 'node_modules/';


exports = module.exports = {
    staticUrlRoot: '/site_media/static',
    paths: {
        source: staticSource,
        build: staticBuild,
        dist: staticDist
    },
    watch: {
        styles: [
            staticSource + 'less/**/*.less'
        ],
        scripts: [
            staticSource + 'js/**/*.js'
        ]
    },
    templates: {
        destination: templatePath,
        manifestPath: staticBuild + 'manifest.json',
        scriptsTemplate: staticSource + 'hbs/_scripts.hbs',
        stylesTemplate: staticSource + 'hbs/_styles.hbs',
        bpmn_des: 'bpmn/templates/',
        bpmn_scriptsTemplate: staticSource + 'hbs/_bpmnscripts.hbs',
        edit_scriptsTemplate: staticSource + 'hbs/_editscripts.hbs',
    },
    fonts: {
        sources: [
            npmRoot + 'font-awesome/fonts/**.*',
            npmRoot + 'bootstrap/fonts/**.*',
        ],
        dist: staticDist + 'fonts/'
    },
    styles: {
        source: staticSource + 'less/site.less',
        dist: staticBuild + 'css/',
        npmPaths: [
            npmRoot + 'bootstrap/less',
            npmRoot + 'font-awesome/less',
            npmRoot
        ]
    },
    scripts: {
        main: staticSource + 'js/site.js',
        bpmnjs: staticSource + 'js/bpmnshow.js',
        editbpmn: staticSource + 'js/editbpmn.js',
        source: [
            staticSource + 'js/**/*'
        ],
        dist: staticBuild + 'js/',
        copy_sources: [
            staticSource + 'js/*.min.js'
        ],
        copyto_dist: staticDist + 'js/'
    },
    images: {
        sources: [
            staticSource + 'images/**.*'
        ],
        dist: staticDist + 'images/'
    },
    less: {
        sources: [
            staticSource + 'less/vendor/**/*'
        ],
        dist: staticDist + 'css/vendor/'
    },
    manifest: {
        source: [
            staticBuild + '**/*.css',
            staticBuild + '**/*.js'
        ]
    },
    test: {
        all: 'test/**/*.test.js',
        req: 'test/req/*.test.js',
        components: 'test/components/*.test.js'
    },
    xo: {
        source: [
            'tasks/**/*.js',
            staticSource + '**/*.js'
        ]
    },
    optimize: {
        css: {
            source: staticDist + 'css/*.css',
            options: {},
            dist: staticDist + 'css/'
        },
        js: {
            source: staticDist + 'js/*.js',
            options: {},
            dist: staticDist + 'js/'
        }
    }
};