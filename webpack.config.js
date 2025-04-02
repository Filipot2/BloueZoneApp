const path = require("path")

module.exports = {
    entry : path.resolve(__dirname,'src'),

    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, 'lecture_manager','lecture_manager', 'static', 'js')
    },
    mode: "development",

    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"]
            }
        ]
    }

}