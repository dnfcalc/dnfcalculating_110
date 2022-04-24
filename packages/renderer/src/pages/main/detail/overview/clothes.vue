<script lang="tsx">
  import { defineComponent, renderList } from "vue"

  export default defineComponent({
    name: "clothes",
    setup(props, { emit, slots }) {
      return () => (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="row-name">武器装扮</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">皮肤</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">光环</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">头发</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">头部</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">脸部</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">胸部</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">上衣</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">腰带</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">下装</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">鞋</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">套装</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <div class="flex-1"></div>
          </div>
        </div>
      )
    }
  })
</script>
