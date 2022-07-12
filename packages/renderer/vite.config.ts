import vue from "@vitejs/plugin-vue"
import jsx from "@vitejs/plugin-vue-jsx"
import path from "path"
import unocss from "unocss/vite"
import uncomponents from "unplugin-vue-components/vite"
import { defineConfig } from "vite"
import pkg from "../../package.json"

import { presetUno } from "unocss"

// https://vitejs.dev/config/
export default defineConfig({
  mode: process.env.NODE_ENV,
  root: __dirname,
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  },
  define: {
    APP_VERSION: `"${pkg.version}"`
  },
  plugins: [
    unocss({
      rules: [
        [
          /^col-(\d?\d)$/,
          ([, o]) => {
            let span = Number(o)
            const val = `${(span * 100) / 24}%`
            return {
              flex: `0 0 ${val}`
            }
          }
        ]
      ],

      presets: [presetUno()]
    }),
    uncomponents({
      dts: true,
      dirs: ["src/components/"],
      allowOverrides: true,

      directoryAsNamespace: true
    }),
    jsx(),
    vue()
  ],

  optimizeDeps: {
    exclude: ["electron"]
  },
  build: {
    sourcemap: process.env./* from mode option */ NODE_ENV == "development",
    outDir: "../../dist/app/renderer",
    assetsDir: "assets"
    // rollupOptions: {
    //   output: {
    //     // 重点在这里哦
    //     // entryFileNames: `assets/[name].${timestamp}.js`,
    //     // chunkFileNames: `assets/[name].${timestamp}.js`,
    //     // assetFileNames: `assets/[name].${timestamp}.[ext]`
    //     // entryFileNames: `assets/[name].js`,
    //     // chunkFileNames: `assets/[name].js`,
    //     assetFileNames: `assets/[name].[ext]`
    //   }
    // }
  },
  server: {
    host: pkg.env.VITE_DEV_SERVER_HOST,
    port: pkg.env.VITE_DEV_SERVER_PORT
  }
})
