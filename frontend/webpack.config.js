const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: "./src/index.js", // Path to your JS entry point
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: "babel-loader",
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./public/index.html", // Use this as a template
      filename: "index.html", // Output file
    }),
  ],
  devServer: {
    static: {
      directory: path.join(__dirname, "dist"),
    },
    port: 8080,
    open: true,
  },
};