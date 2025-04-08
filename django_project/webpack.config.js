const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');

const mode = process.argv.indexOf("production") !== -1 ? "production" : "development";
console.log(`Webpack mode: ${mode}`);

let plugins = [
  new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
  new MiniCssExtractPlugin({
    filename: 'css/[name].[contenthash].css',
  }),
  new webpack.ProvidePlugin({
    $: 'jquery',
    jQuery: 'jquery',
    'window.jQuery': 'jquery',
  }),
  new webpack.ProvidePlugin({
    Leaflet: 'leaflet',
  }),
];

if (mode === 'development') {
  // Only add LiveReloadPlugin in development mode
  const LiveReloadPlugin = require('webpack-livereload-plugin');
  plugins.push(new LiveReloadPlugin({ appendScriptTag: true }));
}

// List of libraries to expose globally
const exposeLibraries = [
  { name: 'jquery', exposes: ['$', 'jQuery'] },
  { name: 'datatables.net', exposes: ['DataTable'] },
  { name: 'moment', exposes: ['moment'] },
  { name: 'leaflet', exposes: ['Leaflet'] },
];


module.exports = {
  entry: './base/static/js/index',
  output: {
    path: path.resolve('./base/static/bundles'),
    filename: "[name].[contenthash].js",
  },
  plugins: plugins,
  module: {
    rules: [
      // Auto-generate expose-loader rules
      ...exposeLibraries.map(lib => ({
        test: require.resolve(lib.name),
        loader: 'expose-loader',
        options: {
          exposes: lib.exposes,
        },
      })),
      // CSS and SCSS rules
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
          },
          {
            loader: 'sass-loader',
            options: {
              sourceMap: true,
            },
          },
        ],
      },
    ],
  },
  stats: {
    assets: false,           // Hide assets info
    chunks: false,           // Hide chunks info
    modules: false,          // Hide modules info
    entrypoints: false,      // Hide entrypoints info
    performance: false,      // Hide performance info
    errors: true,            // Show only errors
    errorDetails: true,      // Include detailed error messages
    warnings: true,          // Show warnings
    builtAt: true,           // Show when the build was created
    colors: true,            // Colorized output
  },
};