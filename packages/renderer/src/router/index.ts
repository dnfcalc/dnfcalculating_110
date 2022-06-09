import { createRouter, createWebHashHistory, createWebHistory } from "vue-router"
import type { RouteRecordRaw } from "vue-router"

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    name: "home",
    component: () => import("@/pages/home.vue")
  },

  {
    path: "/character",
    redirect: "/character/equips",
    name: "main",
    component: () => import("@/pages/main/main.vue"),
    children: [
      {
        path: "/character/skills",
        name: "skill",
        // meta: {
        //   title: "角色"
        // },
        component: () => import("@/pages/main/character/character.vue"),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/equips",
        name: "equipment",
        component: () => import("@/pages/main/equipment/equipment.vue"),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/profile",
        name: "profile",
        component: () => import("@/pages/main/detail/detail.vue"),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/customize",
        name: "customize",
        component: () => import("@/pages/main/customize/customize.vue"),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/singleset",
        name: "singleset",
        component: () => import("@/pages/main/singleset/singleset.vue"),
        meta: {
          keepAlive: true
        }
      }
    ]
  },
  {
    path: "/result",
    name: "result",
    component: () => import("@/pages/result.vue")
  }
]

if (import.meta.env.DEV) {
  //用于组件展示的页面
  routes.push({
    path: "/show",
    name: "show",
    meta: {
      title: "组件展示"
    },
    component: () => import("@/pages/show.vue")
  })

  routes.push({
    path: "/panel/custom_selection",
    name: "custom_selection",
    component: () => import("@/pages/panel/custom_selection.vue")
  })
}

const router = createRouter({
  routes,
  history: createWebHashHistory()
  // history: createWebHistory()
})

export default router
