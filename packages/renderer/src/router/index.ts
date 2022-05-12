import { createRouter, createWebHashHistory } from "vue-router"
import type { RouteRecordRaw } from "vue-router"

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    name: "home",
    component: () => import("@/pages/home/home.vue")
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
        component: () => import("@/pages/main/character/character.vue")
      },
      {
        path: "/character/equips",
        name: "equipment",
        component: () => import("@/pages/main/equipment/equipment.vue")
      },
      {
        path: "/character/profile",
        name: "profile",
        component: () => import("@/pages/main/detail/detail.vue")
      },
      {
        path: "/character/singleset",
        name: "singleset",
        component: () => import("@/pages/main/singleset/singleset.vue")
      }
    ]
  },
  {
    path: "/panel/custom_selection",
    name: "custom_selection",
    component: () => import("@/pages/panel/custom_selection.vue")
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
    component: () => import("@/components/show.vue")
  })
}

const router = createRouter({
  routes,
  history: createWebHashHistory()
})

export default router
