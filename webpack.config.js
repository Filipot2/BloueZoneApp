const path = require("path")

module.exports = {
    entry : "./src/index.js",

    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, 'lecture_manager','lecture_manager', 'static', 'js')
    },
    mode: "development"
}