const App ={
    data() {
        return {
            countrycode: "",
            CVdata: [],
            renewrsp: ""
        }
    },
    methods: {
        getCovidsByCountry(codefilter){
            if (codefilter > ""){
                axios.get('http://back:8000/data/?ordering=-date_value' + '&country_code=' + codefilter)
                .then(response => this.CVdata = response.data)
            }
        },
        renewData(){
            axios.get('http://back:8000/renew/')
            .then(response => this.renewrsp = response.data)
        } 
    }
}

Vue.createApp(App).mount('#app')