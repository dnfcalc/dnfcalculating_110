import type { RouteRecordRaw } from "vue-router"
import { createRouter, createWebHistory } from "vue-router"

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
    path: "/set",
    name: "set",
    component: () => import("@/pages/set.vue")
  },
  {
    path: "/character",
    redirect: "/character/equips",
    name: "main",
    component: () => import("@/pages/character/main.vue"),
    children: [
      {
        path: "/character/skills",
        name: "skills",
        component: () => import("@/pages/character/skills/skills.vue"),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/equips",
        name: "equipment",
        component: () => import("@/pages/character/equipment/equipment.vue"),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/profile",
        name: "profile",
        component: () => import("@/pages/character/detail/detail.vue"),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/customize",
        name: "customize",
        component: () => import("@/pages/character/customize/customize.vue"),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/singleset",
        name: "singleset",
        component: () => import("@/pages/character/singleset/singleset.vue"),
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
  },
  {
    path: "/ranking",
    name: "ranking",
    component: () => import("@/pages/ranking.vue")
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
  history: createWebHistory()
})

export default router
