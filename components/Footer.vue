<template>
  <div class="footer">
    <ul>
      <li v-for="(date, index) in footer_list" :key="index">
        <a :href="date.link" target="_self" v-if="date.is_site">{{ date.title }}</a>
        <router-link :to="date.link" v-else>{{date.title}}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data(){
    return{
      footer_list: []
    }
  },
  methods:{
    get_all_footer(){
      this.$axios({
        method: 'get',
        url: this.$settings.HOST+'home/footers/',
      }).then(res=>{
        this.footer_list = res.data;
      }).catch(error=>{
        console.log(error)
      })
    },
  },
  created() {
    this.get_all_footer()
  },
}
</script>

<style scoped>
.footer {
  width: 100%;
  height: 128px;
  background: #25292e;
  color: #fff;
}

.footer ul {
  margin: 0 auto 16px;
  padding-top: 38px;
  width: 810px;
}

.footer ul li {
  float: left;
  width: 112px;
  margin: 0 10px;
  text-align: center;
  font-size: 14px;
}
</style>