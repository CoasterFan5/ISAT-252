# APIs

## Primary Themes / Topics for the week
- Communicate with the internet
- getting up-to-date information

## Careful With APIs
- Reliability
  - Not all APIs are reliable
  - Free APIs may not always be there
- Security
  - Make sure data you send is secure
  - Worry about where you are sending data
  - Worry about channel where you are sending information
- Ethics and Rate Limits
  - Most APIs have rules about how often you can request information
  - If you over use the service, you may be kicked off or banned

## Why learn APIs now?
- Gateway to making programs interact with the real world
- Instead of working with static, local data, your programs can now:
  - Get live information
  - Interact with popular services and platforms. 

## JSON
- JSON is commonly used in APIs to transmit data between servers and applications
- For instance, when you check the weather on your smartphone, the app probably fetches from a weather API in JSON format. 
- Example
  - ```JSON
    {
        "name": "Alice",
        "age": 25,
        birthday: {
            "month": 12,
            "day", 25,
            "year", 2001
        }
    }

## Example: Weather API
```JSON
{
  "city": "New York",
  "temperature": 15.5,
  "conditions": "Cloudy",
  "forecast": ["Rain", "Sunny", "Cloudy"]
}
```